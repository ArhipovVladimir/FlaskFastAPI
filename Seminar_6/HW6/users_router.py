from models import *
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, HTTPException
from fastapi import Request
from db import *
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()


# Создание тестовых пользователей
@router.get("/fake_users/{count}", summary='фейковые пользователи')
async def create_note(count: int):
    for i in range(1, count + 1):
        query = users_db.insert().values(first_name=f'first_name{i}', last_name=f'last_name{i}',
                                         username=f'username_{i}', email=f'mail_{i}@mail.ru')
        await db.execute(query)
    return {'message': f'{count} fake users create'}


# Создание нового пользователя
@router.post("/users/new/", response_model=User, summary='добавление пользователей')
async def create_user(user: InputUser):
    query = users_db.insert().values(**user.dict())
    last_record_id = await db.execute(query)
    return {**user.dict(), "id": last_record_id}


# Список пользователей
@router.get("/users/", response_model=list[User], summary='Просмотр всех пользователей в JSON')
async def read_users():
    query = users_db.select()
    return await db.fetch_all(query)


# Просмотр одного пользователя
@router.get("/users/id/{user_id}", response_model=User, summary='Просмотр одного пользователя')
async def read_user(user_id: int):
    query = users_db.select().where(users_db.c.id == user_id)
    return await db.fetch_one(query)


# Редактирование пользователя
@router.put("/users/replace/{user_id}", response_model=User, summary='изменение пользователя')
async def update_user(user_id: int, new_user: InputUser):
    query = users_db.update().where(users_db.c.id == user_id).values(**new_user.dict())
    await db.execute(query)
    return {**new_user.dict(), "id": user_id}


# Удаление пользователя
@router.delete("/users/del/{user_id}", summary='Удаление пользователя')
async def delete_user(user_id: int):
    query = users_db.delete().where(users_db.c.id == user_id)
    try:
        await db.execute(query)
        return {'message': 'User deleted'}
    except:
        raise HTTPException(status_code=404, detail="User not found")


# Вывод пользователей в HTML
@router.get("/list_users/", response_class=HTMLResponse, summary='Просмотр пользователей в HTML')
async def list_users(request: Request):
    query = users_db.select()
    return templates.TemplateResponse("Users.html",
                                      {"request": request,
                                       'users': await db.fetch_all(query)})
