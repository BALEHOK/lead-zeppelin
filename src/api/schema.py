import graphene

from src.api.mutation import Mutation
from src.api.query import Query

# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)
