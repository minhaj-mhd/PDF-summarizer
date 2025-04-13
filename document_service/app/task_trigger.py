from celery import Celery
from app.config import BROKER_URL
celery = Celery("client",broker= BROKER_URL)

def send_summary_task(doc_id:str, text:str):
    print("sending task")
    celery.send_task(
        "app.generator.summarize_document",
        args=[doc_id,text],
        queue="summarize"
    )