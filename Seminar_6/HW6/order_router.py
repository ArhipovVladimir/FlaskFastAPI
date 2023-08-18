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


@router.get("/order/join", response_model=list[Order], summary='Просмотр всех ордеро в  JSON')
async def read_order():
    query = orders_db.select().join(users_db).join(items_db)
    print(query)
    result = await db.fetch_all(query)
    print(result)
    return await db.fetch_all(query)


@router.get('/order/', response_model=list[Order], summary='Просмотр всех ордеров запрос')
async def get_post():
    query = sqlalchemy.select(users_db, items_db, orders_db.c.quantity, orders_db.c.status)
    # print(query)
    rows = await db.fetch_all(query)
    return await db.fetch_all(query)

    # res = []
    # for row in rows:
    #     res.append(Post(id=row.id,
    #                     post=row.post,
    #                     user=User(
    #                         id=row.user_id,
    #                         login=row.login,
    #                         password='dsfsdfsdfsdf',
    #                         email='dfdfsfdsf'
    #                         )
    #                     ))
    # return res
    # # return [Post(id=row.id, post=row.post, user=User(id=row.user_id, login=row.login, password='xxxxxx', email='zzzzzz')) for row in rows]


# @router.get("/order/id/{order_id}", response_model=Order, summary='Просмотр одного ордера')
# async def read_order(order_id: int):
#    query = orders_db.select().where(orders_db.c.id == order_id)
#    print(query)
#    print(await db.fetch_one(query))
#    # return await db.fetch_one(query)


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


@router.get("/list_order/select", response_class=HTMLResponse, summary='Просмотр заказовxthtp через запрос в HTML')
async def list_order(request: Request):
    query = sqlalchemy.select(orders_db.c.id, orders_db.c.status, orders_db.c.quantity,
                              items_db.c.id.label('item_id'), items_db.c.name, items_db.c.description, items_db.c.price,
                              users_db.c.id.label('user_id'), users_db.c.first_name.label('fn'), users_db.c.last_name,
                              users_db.c.email).join(
        items_db).join(users_db)
    return templates.TemplateResponse("orders.html",
                                      {"request": request,
                                       'orders': await db.fetch_all(query)})


@router.get("/list_order/selectJSON", response_model=list[Order], summary='JSON через запрос')
async def list_order(request: Request):
    query = sqlalchemy.select(orders_db.c.id, orders_db.c.status, orders_db.c.quantity,
                              items_db.c.id.label('item_id'), items_db.c.name, items_db.c.description, items_db.c.price,
                              items_db.c.quan,
                              users_db.c.id.label('user_id'), users_db.c.first_name, users_db.c.last_name,
                              users_db.c.username, users_db.c.email).join(
        items_db).join(users_db)
    rows = await db.fetch_all(query)
    print(rows)
    return [Order(id=row.id,
                  quantity=row.quantity,
                  status=row.status,
                  user=User(id=row.user_id,
                            last_name=row.last_name,
                            first_name=row.first_name,
                            username=row.username,
                            email=row.email),
                  item=Item(id=row.item_id,
                            name=row.name,
                            price=row.price,
                            quan=row.quan,
                            description=row.description
                            )) for row in rows]
    # return templates.TemplateResponse("orders.html",
    #                                   {"request": request,
    #                                    'orders': await db.fetch_all(query)})



# @router.get("/list_order/", response_class=HTMLResponse, summary='Просмотр заказов в HTML')
# async def list_order(request: Request):
#     query = sqlalchemy.select(orders_db.c.id).join(users_db)
#     print(await db.fetch_all(query))
#     return templates.TemplateResponse("orders.html",
#                                       {"request": request,
#                                        'orders': await db.fetch_all(query)})
#
