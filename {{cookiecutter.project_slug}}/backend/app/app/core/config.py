# import standard library
from os import environ

MONGODB_SETTINGS = {'db': 'app', 'host': 'mongodb', 'port': 27017}
# MONGODB_USER = os.getenv("MONGODB_USER")
# MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")

FIRST_SUPERUSER = environ.get("FIRST_SUPERUSER")
FIRST_SUPERUSER_PASSWORD = environ.get("FIRST_SUPERUSER_PASSWORD")

# Celery/RabbitMQ config
QUEUE_HOST = environ.get('QUEUE_HOST')
if QUEUE_HOST is None:
    QUEUE_HOST = 'queue'

RABBITMQ_PORT = '5672'
RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'

BROKER_URL = 'pyamqp://{user}:{pw}@{host}:{port}//'.format(
    user=RABBITMQ_USER, pw=RABBITMQ_PASS, host=QUEUE_HOST, port=RABBITMQ_PORT)
