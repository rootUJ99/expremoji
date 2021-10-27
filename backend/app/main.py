from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings
from app.api.start import api

def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    @_app.on_event("startup")
    async def startup_db_client():
        _app.mongodb_client = AsyncIOMotorClient(settings.DATABASE_URI)
        _app.mongodb = app.mongodb_client[settings.DB_NAME]
        print('-------------------------------')
        print('-------------------------------')
        print(settings.DATABASE_URI, settings.DB_NAME)
        print('-------------------------------')
        print('-------------------------------')


    @_app.on_event("shutdown")
    async def shutdown_db_client():
        _app.mongodb_client.close()

    return _app


app = get_application()

# app.openapi_url="/api/v1/start/openapi.json"
app.docs_url="/api/v1/start/docs"
app.include_router(api, prefix='/api/v1/start', tags=['start'])
