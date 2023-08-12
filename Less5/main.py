from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import logging
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# @app.get("/")
# async def read_root():
#     logger.info('Отработал GET запрос.')
#     return {"Hello": "World"}
#

@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id ={item_id}.')
    return {"item_id": item_id}


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/itemss/{item_id}")
async def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/users/{user_id}/orders/{order_id}")
async def read_item(user_id: int, order_id: int):
    # обработка данных
    return {"user_id": user_id, "order_id": order_id}


@app.get("/items6/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"


@app.get("/message")
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)


@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    print(request)
    return templates.TemplateResponse("user.html", {"request": request, "name": name})





