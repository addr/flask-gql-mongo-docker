# Import installed packages
from celery import Celery, signals
from kombu import Exchange, Queue
from mongoengine import connect

# Import app code
from app.core.config import BROKER_URL, MONGODB_SETTINGS

CELERY_CONF_UPDATES = dict(
    result_expires=3600,
    task_serializer='json',
    result_serializer='json',
    accept_content={'json'},
    task_default_queue='worker',
    task_queues=(Queue('worker', Exchange('worker'), routing_key='worker'), ),
    task_soft_time_limit=60 * 30)

includes = {
    'include': [
        'app.worker.tasks',
        # The follow is needed to be able to kick off monitor
        #  tasks from engine tasks.
        'app.monitor.tasks'
    ]
}

celery_app = Celery('app', broker=BROKER_URL, backend='rpc://', **includes)

celery_app.conf.update(**CELERY_CONF_UPDATES)


@signals.worker_process_init.connect
def init_worker(**kwargs):
    """Initializes mongoengine connection for each worker
    """
    connect(MONGODB_SETTINGS['db'], host=MONGODB_SETTINGS['host'])


if __name__ == '__main__':
    celery_app.start()
