from graphene_mongo import MongoengineObjectType
from graphene.relay import Node
from graphene import InputObjectType, String, ID, Boolean, List

from app.models.role import Role as RoleModel


class Role(MongoengineObjectType):
    class Meta:
        model = RoleModel
        interfaces = (Node, )


class RoleFilter(InputObjectType):
    q = String()
    id = ID()
    ids = List(ID)
    name = String()
