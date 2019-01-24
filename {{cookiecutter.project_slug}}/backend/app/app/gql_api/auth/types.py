from graphene import ObjectType, String, Int


class Payload(ObjectType):
    email = String()
    exp = Int()
    orig_iat = Int()
