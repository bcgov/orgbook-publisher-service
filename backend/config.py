from pydantic_settings import BaseSettings
import os
import logging
from logging import Logger
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Settings(BaseSettings):
    PROJECT_TITLE: str = "UNTP Publisher"
    PROJECT_VERSION: str = "v0"

    LOG_LEVEL: int = logging.INFO
    LOG_FORMAT: str = "%(asctime)s | %(levelname)-8s | %(module)s:%(funcName)s:%(lineno)d | %(message)s"
    LOGGER: Logger = logging.getLogger(__name__)
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

    DOMAIN: str = os.getenv("DOMAIN")

    TRACTION_API_URL: str = os.getenv("TRACTION_API_URL")
    TRACTION_API_KEY: str = os.getenv("TRACTION_API_KEY")
    TRACTION_TENANT_ID: str = os.getenv("TRACTION_TENANT_ID")

    REGISTRY_URL: str = os.getenv("REGISTRY_URL") or os.getenv("ORGBOOK_URL") or ""  # ORGBOOK_URL backward compat
    REGISTRY_SYNC: bool = os.getenv("REGISTRY_SYNC", os.getenv("ORGBOOK_SYNC", "true")).lower() in ("true", "1", "yes")

    DID_WEB_SERVER_URL: str = os.getenv("DID_WEB_SERVER_URL")
    PUBLISHER_MULTIKEY: str = os.getenv("PUBLISHER_MULTIKEY")

    ISSUER_REGISTRY_URL: str = os.getenv("ISSUER_REGISTRY_URL")

    SECRET_KEY: str = TRACTION_API_KEY
    JWT_SECRET: str = TRACTION_API_KEY
    JWT_ALGORITHM: str = "HS256"

    MONGO_HOST: str = os.getenv("MONGO_HOST")
    MONGO_PORT: str = os.getenv("MONGO_PORT")
    MONGO_USER: str = os.getenv("MONGO_USER")
    MONGO_PASSWORD: str = os.getenv("MONGO_PASSWORD")
    MONGO_DB: str = os.getenv("MONGO_DB")

settings = Settings()
