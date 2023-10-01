"""
### 概要:

    このモジュールには、アプリケーションの設定が含まれています。
"""

# Third Party Library
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings

# First Party Library
from modules.logging_config import configure_logging

logger = configure_logging()


class Settings(BaseSettings):
    """
    ### 概要:

        このクラスは、アプリケーションの設定を定義します。

        設定は、環境変数から読み込まれます。
    """

    title: str = Field(default="FastAPI")
    description: str = Field(default="My App Description")
    version: str = Field(default="1.0.0")
    openapi_url: str = Field(default="/openapi.json")
    docs_url: str = Field(default="/docs")
    prefix_url: str = Field(default="")

    class Config:
        """
        ### 概要:

            このクラスは、設定の構成を定義します。
        """

        env_file = ".env"
        env_file_encoding = "utf-8"


try:
    settings = Settings()
except ValidationError as e:
    logger.error(e)
