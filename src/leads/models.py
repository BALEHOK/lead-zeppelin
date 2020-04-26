from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr

db = SQLAlchemy()


class UuidMixin(object):
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))


class AccountRelatedMixin(UuidMixin):
    @declared_attr
    def account_id(cls):
        return db.Column(UUID(as_uuid=True), db.ForeignKey('accounts.id'))


class TimestampMixin(object):
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)


class Account(UuidMixin, TimestampMixin, db.Model):
    __tablename__ = 'accounts'
    name = db.Column(db.String(256))
    code = db.Column(db.String(15))
    api_tokens = db.relationship('ApiToken', backref='account')
    clients = db.relationship('Client', backref='account')
    funnels = db.relationship('Funnel', backref='account')


class ApiToken(AccountRelatedMixin, TimestampMixin, db.Model):
    __tablename__ = 'tokens'
    name = db.Column(db.String(256))
    token = db.Column(db.String(256))


class Lead(UuidMixin, TimestampMixin, db.Model):
    __tablename__ = 'leads'
    client_id = db.Column(UUID(as_uuid=True), db.ForeignKey('clients.id'))
    source = db.Column(db.String(256))
    medium = db.Column(db.String(256))
    campaign = db.Column(db.String(256))
    content = db.Column(db.String(256))
    funnel_step_id = db.Column(UUID(as_uuid=True), db.ForeignKey('funnel_steps.id'))
    funnel_step = db.relationship("FunnelStep", back_populates='leads')


    def __repr__(self):
        return '<Lead %r>' % self.user


class Client(AccountRelatedMixin, TimestampMixin, db.Model):
    __tablename__ = 'clients'
    name = db.Column(db.String(256))
    email = db.Column(db.String(256))
    phone = db.Column(db.String(256))
    vk = db.Column(db.String(256))
    fb = db.Column(db.String(256))
    gc = db.Column(db.String(256))
    leads = db.relationship('Lead', backref='client')
    payments = db.relationship('Payment', back_populates='client')

    def __repr__(self):
        return '<User %r>' % self.name


class Funnel(AccountRelatedMixin, db.Model):
    __tablename__ = 'funnels'
    name = db.Column(db.String(256))
    steps = db.relationship('FunnelStep', backref='funnel')


class FunnelStep(UuidMixin, db.Model):
    __tablename__ = 'funnel_steps'
    name = db.Column(db.String(256))
    code = db.Column(db.String(15))
    funnel_id = db.Column(UUID(as_uuid=True), db.ForeignKey('funnels.id'))
    leads = db.relationship("Lead", back_populates='funnel_step')


class LeadFunnelStepHistory(UuidMixin, db.Model):
    __tabelname__ = 'lead_funnel_step_history'
    prev_step_id = db.Column(UUID(as_uuid=True), db.ForeignKey('funnel_steps.id'), nullable=True)
    funnel_step_id = db.Column(UUID(as_uuid=True), db.ForeignKey('funnel_steps.id'), nullable=True)
    lead_id = db.Column(UUID(as_uuid=True), db.ForeignKey('leads.id'))
    changed = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)


class Payment(UuidMixin, TimestampMixin, db.Model):
    __tablename__ = 'client_payment'
    client_id = db.Column(UUID(as_uuid=True), db.ForeignKey('clients.id'))
    client = db.relationship("Client", back_populates='payments')
    lead_id = db.Column(UUID(as_uuid=True), db.ForeignKey('leads.id'), nullable=True)
    amount = db.Column(db.Integer())
