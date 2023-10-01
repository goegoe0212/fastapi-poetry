# Third Party Library
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings

# First Party Library
from modules.logging_config import configure_logging

logger = configure_logging()


class Settings(BaseSettings):
    title: str = Field(default="FastAPI")
    description: str = Field(default="My App Description")
    version: str = Field(default="1.0.0")
    openapi_url: str = Field(default="/openapi.json")
    docs_url: str = Field(default="/docs")
    prefix_url: str = Field(default="")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


try:
    settings = Settings()
except ValidationError as e:
    logger.error(e)
