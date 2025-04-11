from celery import Celery
from app.config import BROKER_URL

celery = Celery("summerizer",broker=BROKER_URL,backend = BROKER_URL)
celery.conf.task_routes = {
    "app.services.generator.summerize_document": {"queue":"summerize"}
}