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
