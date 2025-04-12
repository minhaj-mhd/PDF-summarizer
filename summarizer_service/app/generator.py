from transformers import pipeline
from app.config import MODEL_NAME,MONGO_DB,MONGO_URI
from app.celery_worker import celery
from pymongo import MongoClient
from bson import ObjectId

summerizer = pipeline("summarization", model = MODEL_NAME)

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]


def generate_summary(text: str) -> str:
    result = summerizer(text, max_length = 300, min_length = 50, do_sample=False)
    return result[0]['summery_text']

@celery.task(name = "app.generator.summarize_document")
def summarize_document(document_id:str, content:str):
    summary = generate_summary(content)
    print(summary)
    db.summaries.insert_one({
        "document_id":ObjectId(document_id),
        "summary":summary
    })
    db.documents.update_one({"_id":ObjectId(document_id)},{"$set":{"status":"summarized"}})