from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer_question(summary : str, question : str ) -> str:
    result = qa_pipeline(context = summary, question = question)
    return result["answer"]