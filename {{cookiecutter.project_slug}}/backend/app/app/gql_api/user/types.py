from graphene_mongo import MongoengineObjectType
from graphene.relay import Node
from graphene import ObjectType, InputObjectType, String, ID, Boolean, List, Int

from app.models.user import User as UserModel


class User(MongoengineObjectType):
    class Meta:
        model = UserModel
        interfaces = (Node, )


class UserFilter(InputObjectType):
    q = String()
    id = ID()
    ids = List(ID)
    firstName = String()
    lastName = String()
    email = String()
    active = Boolean()
