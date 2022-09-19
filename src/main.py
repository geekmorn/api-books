from fastapi import FastAPI
from .common.config.settings import settings
from .common.config.database import db
from .api.routers import api_router

app = FastAPI(
    docs_url=settings.DOCS_URL,
    title=settings.TITLE,
    version=settings.VERSION
)

app.include_router(api_router)


@app.on_event("startup")
async def startup():
    db.create()
    await db.create_table()


@app.on_event("shutdown")
async def shutdown():
    await db.close()
