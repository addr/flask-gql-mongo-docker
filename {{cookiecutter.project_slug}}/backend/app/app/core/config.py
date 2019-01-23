# import standard library
import os

MONGODB_SETTINGS = {'db': 'app', 'host': 'mongodb', 'port': 27017}
# MONGODB_USER = os.getenv("MONGODB_USER")
# MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")

FIRST_SUPERUSER = os.getenv("FIRST_SUPERUSER")
FIRST_SUPERUSER_PASSWORD = os.getenv("FIRST_SUPERUSER_PASSWORD")
