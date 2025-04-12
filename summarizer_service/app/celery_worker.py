from celery import Celery
from app.config import BROKER_URL

celery = Celery("summarizer",broker=BROKER_URL,backend = BROKER_URL)
celery.conf.task_routes = {
    "app.generator.summarize_document": {"queue":"summarize"}
}

celery.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json']
)