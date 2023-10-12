from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List


class Tag(BaseSettings):
    name: str
    description: str


class AppDescription(BaseSettings):
    title: str = "Bewise API"
    description: str = "API для получения вопросов викторины"
    version: str = "1.0.0"
    debug: bool = False
    openapi_tags: List[Tag] = [Tag(name="Questions", description="Question endpoints")]


@lru_cache
class Settings(BaseSettings):
    """ Креды для БД подгружаются из .env """
    DB_USER: str
    DB_PASSWORD: str
    DB_SCHEMA: str
    DB_HOST: str
    DB_PORT: str
    DB_URL: str
    app_description: AppDescription = AppDescription()

    class Config:
        env_file = ".env"
