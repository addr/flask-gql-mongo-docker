from .init_worker import celery_app


@celery_app.task(name="test_worker", bind=True)
def test_worker(self):
    return "Celery worker test task"
