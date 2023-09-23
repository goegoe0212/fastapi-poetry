# Third Party Library
from fastapi import APIRouter
from fastapi.responses import JSONResponse

app = APIRouter()


@app.get("/")
def read_root() -> JSONResponse:
    data = {"Hello": "World"}
    return JSONResponse(data)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> JSONResponse:
    data = {"item_id": item_id, "q": q}
    return JSONResponse(data)
