from fastapi import FastAPI
from app.summarizer import router as summerizer_router

app = FastAPI()
app.include_router(summerizer_router, prefix="/summarize", tags = ["Summarizer"])