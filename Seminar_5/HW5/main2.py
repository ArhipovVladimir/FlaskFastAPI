

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
from fastapi import HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


class UserIn(BaseModel):
    name: str
    email: str
    password: str

class User(UserIn):
    id: int


users = []


# response_model - то, что возвращает endpoint
# @app.get("/", response_model=list[User], summary='Получить список пользователей', tags=['Пользователи'])
# async def read_user():
#     return users


@app.get("/", response_class=HTMLResponse, summary='Получить список пользователей', tags=['Пользователи'])
async def read_item(request: Request):
    print(request)
    return templates.TemplateResponse("user.html", {"request": request, "users": users})

# response_model - то, что возвращает endpoint


@app.post("/user/", response_model=User, tags=['Пользователи'])
async def delete_user(request: Request, user_id: int = Form(...)):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            break
    return templates.TemplateResponse("user.html", {"request": request, "users": users})


@app.post("/process_form", response_model=User, summary='добавление пользователей', tags=['Пользователи'])
# в аргументах - то, что принимаем
async def create_user(request: Request):
    form_tata = await request.form()
    name = form_tata.get("name")
    email = form_tata.get("email")
    password = form_tata.get("password")
    users.append(
        User(id=len(users) +1,
             name=name,
             email=email,
             password=password
             )
    )
    return templates.TemplateResponse('form_success.html', {"request": request})


@app.get("/user/{id}", response_model=User, summary='Получить пользователя', tags=['Пользователи'])
async def get_user_by_id_root(id: int):
    for user in users:
        if user.id == id:
            return user


@app.put("/user/{id}", response_model=User, summary='изменить пользователя', tags=['Пользователи'])
async def put_user_by_id_root(id: int, new_user: UserIn):
    for user in users:
        if user.id == id:
            user.name = new_user.name
            user.email = new_user.email
            user.password = new_user.password
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{id}", summary='Удалить пользователя', tags=['Пользователи'])
async def delete_user(id: int):
    for user in users:
        if user.id == id:
            users.remove(user)
            return users
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
