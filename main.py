"""
### 概要:

    このモジュールには、FastAPIアプリケーションのメイン部分が含まれています。

    FastAPIアプリケーションは、`fastapi`モジュールの`FastAPI`クラスを使用して作成されます。
    アプリケーションには、`router_hello`ルーターが含まれ、`settings`モジュールからの設定で構成されています。

### 属性:

    app (FastAPI): メインのFastAPIアプリケーションインスタンス。

### 使用例:
    - Production:
    アプリケーションを起動するには、Docker composeを使用します。
    - Development:
    VSCodeのデバッグ機能を使用して、アプリケーションを起動します。
"""


# Third Party Library
from fastapi import FastAPI

# First Party Library
from routers import router_hello
from settings.setting import settings

app = FastAPI(
    title=settings.title,
    description=settings.description,
    version=settings.version,
    openapi_url=settings.openapi_url,
    docs_url=settings.docs_url,
    redoc_url=None,
)

app.include_router(router_hello.app, prefix=settings.prefix_url)
