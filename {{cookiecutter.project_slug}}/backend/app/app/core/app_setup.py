# Import standard library
# Import installed
# Import app code
from app.main import app
from app.db.init_db import init_db
from app.core import config

from . import cors

init_db()
