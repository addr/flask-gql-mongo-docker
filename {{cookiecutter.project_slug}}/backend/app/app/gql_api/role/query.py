from graphene import List

from app.gql_api.base import BaseQuery
from .types import Role, RoleFilter
from . import resolvers as resolve


class Query(BaseQuery):
    all_roles = BaseQuery.QueryList(
        Role, RoleFilter, resolver=resolve.all_roles)
    all_roles_meta = BaseQuery.ListMetaField(
        RoleFilter, name="_allRolesMeta", resolver=resolve.all_roles_meta)
    Role = BaseQuery.SingleField(Role)
