from flask import abort
from flask_jwt_extended import get_current_user, jwt_required

from app.models.user import User
from app.gql_api.list_metadata.types import ListMetadata
from app.gql_api.base import default_query_resolver


def all_users(self,
              info,
              page=None,
              perPage=10,
              sortField=None,
              sortOrder=None,
              filter=None,
              **kwargs):
    current_user = get_current_user()
    if not current_user:
        abort(400, "Couldn't authenticate user with provided token")
    return default_query_resolver(User, page, perPage, sortField, sortOrder,
                                  filter)


def all_users_meta(self,
                   info,
                   page=None,
                   perPage=10,
                   sortField=None,
                   sortOrder=None,
                   filter=None,
                   **kwargs):
    return ListMetadata(count=User.objects.count())
