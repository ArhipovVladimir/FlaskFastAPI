from models import *
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from fastapi import Request
from db import *
from fastapi.templating import Jinja2Templates
from random import randint, uniform
templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/fake_Item/{count}", summary='фейковые данных')
async def create_item(count: int):
    for i in range(1, count + 1):
        query = items_db.insert().values(name=f'name{i}', price=uniform(1, 100), quan=randint(1, 100), description="description")
        await db.execute(query)
    return {'message': f'{count} fake Item create'}


@router.post("/item/new/", response_model=Item, summary='добавление товара')
async def create_user(item: InputItem):
    query = items_db.insert().values(**item.model_dump())
    last_record_id = await db.execute(query)
    return {**item.dict(), "id": last_record_id}


@router.get("/item/", response_model=list[Item], summary='Просмотр всех товаров в JSON')
async def read_itrm():
    query = items_db.select()
    return await db.fetch_all(query)


@router.get("/item/id/{item_id}", response_model=Item, summary='Просмотр одного товара')
async def read_user(item_id: int):
    query = items_db.select().where(items_db.c.id == item_id)
    return await db.fetch_one(query)


@router.put("/items/replace/{items_id}", response_model=Item, summary='изменение товара')
async def update_user(item_id: int, new_item: InputItem):
    query = items_db.update().where(items_db.c.id == item_id).values(**new_item.dict())
    await db.execute(query)
    return {**new_item.dict(), "id": item_id}


@router.delete("/items/del/{item_id}", summary='Удаление товара')
async def delete_user(item_id: int):
    query = items_db.delete().where(items_db.c.id == item_id)
    await db.execute(query)
    return {'message': 'Item deleted'}


@router.get("/list_items/", response_class=HTMLResponse, summary='Просмотр пользователей в HTML')
async def list_users(request: Request):
    query = items_db.select()
    return templates.TemplateResponse("items.html",
                                      {"request": request,
                                       'items': await db.fetch_all(query)})

