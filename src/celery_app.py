from celery import Celery
from src.config import CONFIG


CELERY_BROKER_URL = f'amqp://{CONFIG.RABBITMQ_USER}:{CONFIG.RABBITMQ_PASSWORD}@rabbitmq:5672//'
celery_app = Celery(
    'derbitclient',
    broker=CELERY_BROKER_URL,
)
celery_app.conf.imports = ('src.app.fetcher',)
celery_app.conf.beat_schedule = {
    'fetch-tickers-every-60-seconds': {
        'task': 'fetch_and_save_tickers',
        'schedule': 60,
    },
}