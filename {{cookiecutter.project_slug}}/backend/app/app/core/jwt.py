# Import standard library modules
from functools import wraps

# Import installed modules
try:
    from flask import _app_ctx_stack as ctx_stack
except ImportError:  # pragma: no cover
    from flask import _request_ctx_stack as ctx_stack
from flask_jwt_extended import JWTManager, verify_jwt_in_request
from flask_jwt_extended.exceptions import (CSRFError, FreshTokenRequired,
                                           InvalidHeaderError,
                                           NoAuthorizationError, UserLoadError)

from app.db.users import get_user

# Import app code
from ..main import app

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)


@jwt.user_loader_callback_loader
def get_current_user(identity):
    return get_user(identity)
