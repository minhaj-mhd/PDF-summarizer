from fastapi import FastAPI
from app.routes import router as document_router



app = FastAPI()
app.include_router(document_router, prefix="/documents", tags=["Documents"])
