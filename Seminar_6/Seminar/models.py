# Разработать API для управления списком пользователей с
# использованием базы данных SQLite. Для этого создайте
# модель User со следующими полями:
# ○ id: int (идентификатор пользователя, генерируется
# автоматически)
# ○ username: str (имя пользователя)
# ○ email: str (электронная почта пользователя)
# ○ password: str (пароль пользователя)

from pydantic import BaseModel, Field


class InputUser(BaseModel):
    login: str = Field(title="Login", min_length=4)
    password: str = Field(title="Password", min_length=6)
    email: str = Field(title="E-mail", min_length=5)


class User(InputUser):
    id: int


class InputPost(BaseModel):
    us_id: int
    post: str


class Post(BaseModel):
    id: int
    user: User
    post: str

