# Import standard library modules

# Import installed modules
from flask_jwt_extended import JWTManager

from app.db.users import get_user

# Import app code
from ..main import app

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)


@jwt.user_loader_callback_loader
def get_current_user(email):
    return get_user(email)
