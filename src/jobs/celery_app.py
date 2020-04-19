from celery import Celery
from mongoengine import connect, register_connection, DEFAULT_CONNECTION_NAME

from src.config import config

celery_app = Celery('lead_zeppelin', broker=config.get('mongo_jobs_uri'))
celery_app.autodiscover_tasks(packages=['src.processes'])
celery_app.broker_connection

# connection fails here
register_connection(alias=DEFAULT_CONNECTION_NAME, host=config.get('mongo_web_uri'))
