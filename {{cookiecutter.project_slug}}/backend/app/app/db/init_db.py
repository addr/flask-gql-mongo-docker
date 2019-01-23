from flask_mongoengine import MongoEngine

# Import app code
from app.main import app
from app.core import config
from app.db.users import create_or_get_user


def init_db():
    app.config['MONGODB_SETTINGS'] = config.MONGODB_SETTINGS
    MongoEngine(app)

    # create first superuser
    create_or_get_user(
        config.FIRST_SUPERUSER,
        config.FIRST_SUPERUSER_PASSWORD,
        is_superuser=True)
