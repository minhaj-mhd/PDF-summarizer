import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
FILE_STORAGE_PATH = os.getenv("FILE_STORAGE_PATH", "./uploaded_docs")