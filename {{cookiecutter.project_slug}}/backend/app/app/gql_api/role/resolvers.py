from app.models.role import Role
from app.gql_api.list_metadata.types import ListMetadata
from app.gql_api.base import default_query_resolver


def all_roles(self,
              info,
              page=None,
              perPage=10,
              sortField=None,
              sortOrder=None,
              filter=None,
              **kwargs):
    return default_query_resolver(Role, page, perPage, sortField, sortOrder,
                                  filter)


def all_roles_meta(self,
                   info,
                   page=None,
                   perPage=10,
                   sortField=None,
                   sortOrder=None,
                   filter=None,
                   **kwargs):
    return ListMetadata(count=Role.objects.count())
