<<<<<<< HEAD
"""
### 概要:

    このモジュールには、アプリケーションの設定が含まれています。
"""

=======
>>>>>>> 2afbdac39218105b771ec970834071971110f80c
# Third Party Library
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings

# First Party Library
from modules.logging_config import configure_logging

logger = configure_logging()


class Settings(BaseSettings):
<<<<<<< HEAD
    """
    ### 概要:

        このクラスは、アプリケーションの設定を定義します。

        設定は、環境変数から読み込まれます。
    """

=======
>>>>>>> 2afbdac39218105b771ec970834071971110f80c
    title: str = Field(default="FastAPI")
    description: str = Field(default="My App Description")
    version: str = Field(default="1.0.0")
    openapi_url: str = Field(default="/openapi.json")
    docs_url: str = Field(default="/docs")
    prefix_url: str = Field(default="")

    class Config:
<<<<<<< HEAD
        """
        ### 概要:

            このクラスは、設定の構成を定義します。
        """

=======
>>>>>>> 2afbdac39218105b771ec970834071971110f80c
        env_file = ".env"
        env_file_encoding = "utf-8"


try:
    settings = Settings()
except ValidationError as e:
    logger.error(e)
