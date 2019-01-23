# Import standard library
# Import installed
# Import app code
from app.main import app
from app.db.init_db import init_db
from app.core import config

from . import cors

from ..gql_api.view import gql_view

init_db()

app.add_url_rule('/graphql', view_func=gql_view())
