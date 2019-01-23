from graphene import ObjectType, Int


class ListMetadata(ObjectType):
    count = Int(required=True)
