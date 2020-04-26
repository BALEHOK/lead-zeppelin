import graphene

from src.web.mutation import Mutation
from src.web.query import Query

# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)
