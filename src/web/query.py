import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from src.leads.models import Lead, Client, Funnel, FunnelStep, LeadFunnelStepHistory, Payment, Account


class AccountObject(SQLAlchemyObjectType):
    class Meta:
        model = Account
        interfaces = (graphene.relay.Node,)


class ClientObject(SQLAlchemyObjectType):
    class Meta:
        model = Client
        interfaces = (graphene.relay.Node,)


class LeadObject(SQLAlchemyObjectType):
    class Meta:
        model = Lead
        interfaces = (graphene.relay.Node,)


class FunnelObject(SQLAlchemyObjectType):
    class Meta:
        model = Funnel
        interfaces = (graphene.relay.Node,)


class FunnelStepObject(SQLAlchemyObjectType):
    class Meta:
        model = FunnelStep
        interfaces = (graphene.relay.Node,)


class LeadFunnelStepHistoryObject(SQLAlchemyObjectType):
    class Meta:
        model = LeadFunnelStepHistory
        interfaces = (graphene.relay.Node,)


class PaymentObject(SQLAlchemyObjectType):
    class Meta:
        model = Payment
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    account = graphene.Field(AccountObject)
    clients = SQLAlchemyConnectionField(ClientObject)
    leads = SQLAlchemyConnectionField(LeadObject)
    funnels = SQLAlchemyConnectionField(FunnelObject)
    funnelSteps = SQLAlchemyConnectionField(FunnelStepObject)
    leadFunnelStepHistories = SQLAlchemyConnectionField(LeadFunnelStepHistoryObject)
    payments = SQLAlchemyConnectionField(PaymentObject)

    @classmethod
    def resolve_account(cls, info, id):
        return Account.query.first()
