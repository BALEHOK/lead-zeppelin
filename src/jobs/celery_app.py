from celery import Celery
from mongoengine import connect

from src.config import config

connect(host=config.get('mongo_web_uri'))
celery_app = Celery('lead_zeppelin', broker=config.get('redis_uri'))
celery_app.autodiscover_tasks(packages=['src.processes'])
