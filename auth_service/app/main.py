from fastapi import FastAPI
from . import models, database
from .route import router

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

app.include_router(router)