from .init_monitor import celery_app


@celery_app.task(
    name="monitor_test", bind=True, default_retry_delay=5, max_retries=None)
def monitor_test(self):
    return "Celery monitor test"
