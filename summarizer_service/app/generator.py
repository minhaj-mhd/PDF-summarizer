from transformers import pipeline
from app.config import MODEL_NAME,MONGO_DB,MONGO_URI
from app.celery_worker import celery
from pymongo import MongoClient
from bson import ObjectId

summerizer = pipeline("summarization", model = MODEL_NAME)

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

def split_text(text, max_chunk_length=1000):
    return [text[i:i+max_chunk_length] for i in range(0,len(text),max_chunk_length)]

def generate_summary(text: str) -> str:
    chunks = split_text(text)

    summaries = []
    for chunk in chunks:
        try:
            result = summerizer(chunk,truncation=True, max_length = 300, min_length = 50, do_sample=False)
            chunk_summary = result[0]['summary_text']
            summaries.append(chunk_summary)
        except Exception as e:
            print(f"Summarization Error {e}")
    return " ".join(summaries)

def get_summary_text(doc_id:str):
    try:
        text = db.summaries.find_one({"document_id":ObjectId(doc_id)})
        return (text["summary"])
    except Exception as e:
        print("Error")

@celery.task(name = "app.generator.summarize_document")
def summarize_document(document_id:str, content:str):
    summary = generate_summary(content)
    print(summary)
    db.summaries.insert_one({
        "document_id":ObjectId(document_id),
        "summary":summary
    })
    db.documents.update_one({"_id":ObjectId(document_id)},{"$set":{"status":"summarized"}})