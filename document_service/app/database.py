from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()
client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]

async def save_document(filename: str, content: str):
    doc = {"filename": filename, "content": content}
    result = await db.documents.insert_one(doc)
    return result.inserted_id
