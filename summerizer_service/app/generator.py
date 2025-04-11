from transformers import pipeline
from app.config import MODEL_NAME

summerizer = pipeline("summarization", model = MODEL_NAME)

def generate_summary(text: str) -> str:
    result = summerizer(text, max_length = 300, min_length = 50, do_sample=False)
    return result[0]['summery_text']