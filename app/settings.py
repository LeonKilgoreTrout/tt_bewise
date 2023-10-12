from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Dict, List, Any


app_description = {
    "title": "Bewise API",
    "description": "API для получения вопросов викторины",
    "version": "1.0.0",
    "debug": True,
    "openapi_tags": [
        {
                "name": "Questions",
                "description": "Question endpoints"
        }
    ]
}


@lru_cache
class Settings(BaseSettings):
    """ Креды для БД подгружаются из .env """
    DB_USER: str
    DB_PASSWORD: str
    DB_SCHEMA: str
    DB_HOST: str
    DB_PORT: str
    DB_URL: str
    app_description: Any = app_description

    class Config:
        env_file = ".env"
