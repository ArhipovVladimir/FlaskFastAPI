from models import *
from sqlalchemy import select
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from fastapi import Request
from db import *
from fastapi.templating import Jinja2Templates
from random import randint
templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/fake_Item/{count}", summary='фейковые данных')
async def create_item(count: int):
    for i in range(1, count + 1):
        query = items_db.insert().values(name=f'name{i}', price=randint(1, 10), qaunliti=randint(1, 10))
        await db.execute(query)
    return {'message': f'{count} fake Item create'}


@router.post("/item/new/", response_model=Item, summary='добавление товара')
async def create_user(item: InputItem):
    query = items_db.insert().values(**item.dict())
    last_record_id = await db.execute(query)
    return {**item.dict(), "id": last_record_id}


@router.get("/item/", response_model=list[Item], summary='Просмотр всех товаров в JSON')
async def read_itrm():
    query = items_db.select()
    result = await db.fetch_all(query)
    print(result)
    return await db.fetch_all(query)


@router.get("/item/id/{item_id}", response_model=Item, summary='Просмотр одного товара')
async def read_user(item_id: int):
    query = items_db.select().where(items_db.c.id == item_id)
    return await db.fetch_one(query)


@router.put("/items/replace/{items_id}", response_model=Item, summary='изменение товара')
async def update_user(item_id: int, new_item: InputItem):
    query = items_db.update().where(item_id.c.id == item_id).values(**new_item.dict())
    await db.execute(query)
    return {**new_item.dict(), "id": item_id}


@router.delete("/items/del/{item_id}", summary='Удаление товара')
async def delete_user(item_id: int):
    query = items_db.delete().where(item_id.c.id == item_id)
    await db.execute(query)
    return {'message': 'Item deleted'}


@router.get("/list_items/", response_class=HTMLResponse, summary='Просмотр пользователей в HTML')
async def list_users(request: Request):
    query = items_db.select()
    return templates.TemplateResponse("Users.html",
                                      {"request": request,
                                       'items': await db.fetch_all(query)})
















#
#
# @router.get('/Items/', response_model=list[Post])
# async def get_post():
#     query = select(
#         Items_db.c.id, Items_db.c.title,
#         users_db.c.id.label("user_id"),
#         users_db.c.usermae).join(users_db)
#     #query = posts_db.select()
#     rows = await db.fetch_all(query)
#     res = []
#     for row in rows:
#         res.append(Post(id=row.id,
#                         post=row.post,
#                         user=User(
#                             id=row.user_id,
#                             login=row.login,
#                             password='dsfsdfsdfsdf',
#                             email='dfdfsfdsf'
#                             )
#                         ))
#     return res
#     # return [Post(id=row.id, post=row.post, user=User(id=row.user_id, login=row.login, password='xxxxxx', email='zzzzzz')) for row in rows]
#
# # ToDo заготовка для ордера
# @router.post('/order/', response_model=dict)
# async def inp_order(order: InputOrder):
#     query = items_db.insert().values(
#         user_id=order.user_id,
#         irem=post.post,)
#     last_record_id = await db.execute(query)
#     return {**order.dict(), "id": last_record_id}
#
