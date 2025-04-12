import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME","")
MONGO_URI = os.getenv("MONGO_URI","mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", 'pdf_ai')
BROKER_URL = os.getenv("BROKER_URL","redis://localhost:6379/0")