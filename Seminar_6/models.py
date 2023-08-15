from pydantic import BaseModel, Field

class InputUser(BaseModel):
    login: str = Field(title="Login", min_length=4)
    password: str = Field(title="Password", min_length=6)
    email: str = Field(title="E-mail", min_length=5)


class User(InputUser):
    id: int

class InputPost(BaseModel):
    us_id : int
    post : str

class Post(BaseModel):
    id : int
    user : User
    post : str

