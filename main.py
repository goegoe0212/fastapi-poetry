from fastapi import FastAPI
from routers import router_hello

app = FastAPI()

app.route(router_hello)
