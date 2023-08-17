from models import *
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from fastapi import Request
from random import randint, choice
from db import *
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/fake_order/{count}", summary='фейковые данных')
async def create_order(count: int):
    for i in range(1, count + 1):
        query = orders_db.insert().values(user_id=randint(1, 15), quantity=randint(1, 100),
                                          item_id=randint(1, 15), status=choice([True, False]))
        print(query)
        await db.execute(query)
    return {'message': f'{count} fake Order create OK'}


@router.post("/order/new/", response_model=Order, summary='добавление ордера')
async def create_order(order: InputOrder):
    query = orders_db.insert().values(**order.model_dump())
    last_record_id = await db.execute(query)
    return {**order.model_dump(), "id": last_record_id}


@router.get("/order/", response_model=list[Order], summary='Просмотр всех ордеро в  JSON')
async def read_order():
    query = orders_db.select().join(users_db).join(items_db)
    print(query)
    result = await db.fetch_all(query)
    print(result)
    return await db.fetch_all(query)



# @router.post('/order/', response_model=dict)
# async def inp_order(order: InputOrder):
#     query = items_db.insert().values(
#         user_id=order.user_id,
#         irem=post.post,)
#     last_record_id = await db.execute(query)
#     return {**order.dict(), "id": last_record_id}
#


@router.get("/order/id/{order_id}", response_model=Order, summary='Просмотр одного ордера')
async def read_order(order_id: int):
    query = orders_db.select().where(orders_db.c.id == order_id)
    return await db.fetch_one(query)


@router.put("/order/replace/{order_id}", response_model=Order, summary='изменение Order')
async def update_user(order_id: int, new_order: InputOrder):
    query = orders_db.update().where(orders_db.c.id == order_id).values(**new_order.model_dump())
    await db.execute(query)
    return {**new_order.model_dump(), "id": order_id}


@router.delete("/order/del/{order_id}", summary='Удаление Заказа')
async def delete_order(order_id: int):
    query = orders_db.delete().where(orders_db.c.id == order_id)
    await db.execute(query)
    return {'message': 'Order deleted'}


@router.get("/list_order/", response_class=HTMLResponse, summary='Просмотр заказов в HTML')
async def list_order(request: Request):
    query = orders_db.select().join(users_db).join(items_db)
    print(await db.fetch_all(query))
    return templates.TemplateResponse("orders.html",
                                      {"request": request,
                                       'orders': await db.fetch_all(query)})


# @router.get("/list_order/", response_class=HTMLResponse, summary='Просмотр заказов в HTML')
# async def list_order(request: Request):
#     query = select(orders_db.c.id).join(users_db)
#     print(await db.fetch_all(query))
#     return templates.TemplateResponse("orders.html",
#                                       {"request": request,
#                                        'orders': await db.fetch_all(query)})
#
# #
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
