import graphene
from cars.schema.schema import Query, Mutation

class Query(Query, graphene.ObjectType):
    """
    Theoretically, merges all queries from all apps.
    """
    pass

class Mutation(Mutation, graphene.ObjectType):
    """
    Theoretically, merges all mutations from all apps.
    """
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
