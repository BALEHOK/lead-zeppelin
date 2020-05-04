import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from src.leads.models import Lead, Client, Funnel, FunnelStep, LeadFunnelStepHistory, Payment


class LeadObject(SQLAlchemyObjectType):
    class Meta:
        model = Lead
        interfaces = (graphene.relay.Node,)


class ClientObject(SQLAlchemyObjectType):
    class Meta:
        model = Client
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
    leads = SQLAlchemyConnectionField(LeadObject)
    clients = SQLAlchemyConnectionField(ClientObject)
    funnels = SQLAlchemyConnectionField(FunnelObject)
    funnelSteps = SQLAlchemyConnectionField(FunnelStepObject)
    LeadFunnelStepHistories = SQLAlchemyConnectionField(LeadFunnelStepHistoryObject)
    payments = SQLAlchemyConnectionField(PaymentObject)
