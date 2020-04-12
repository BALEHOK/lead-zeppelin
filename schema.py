import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from models import Lead, Client


class LeadObject(SQLAlchemyObjectType):
    class Meta:
        model = Lead
        interfaces = (graphene.relay.Node,)


class ClientObject(SQLAlchemyObjectType):
    class Meta:
        model = Client
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_leads = SQLAlchemyConnectionField(LeadObject)
    all_clients = SQLAlchemyConnectionField(ClientObject)