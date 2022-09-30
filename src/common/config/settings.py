from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings


load_dotenv(find_dotenv())


class Settings(BaseSettings):
    PORT: int
    ROUTE_PREFIX: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_DB: str
    DOCS_URL: str
    TITLE: str
    VERSION: str


settings = Settings()
