from graphene import List

from app.gql_api.base import BaseQuery
from .types import User, UserFilter
from . import resolvers as resolve


class Query(BaseQuery):
    all_users = BaseQuery.QueryList(
        User, UserFilter, resolver=resolve.all_users)
    all_users_meta = BaseQuery.ListMetaField(
        UserFilter, name="_allUsersMeta", resolver=resolve.all_users_meta)
    User = BaseQuery.SingleField(User)
