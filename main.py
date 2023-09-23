# Third Party Library
from fastapi import FastAPI

# First Party Library
from routers import router_hello

app = FastAPI()

app.include_router(router_hello.app)
