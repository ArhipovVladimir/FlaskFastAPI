from pydantic import BaseModel, Field
from datetime import datetime


class InputUser(BaseModel):
    first_name: str = Field(title="first_name", max_length=100)
    last_name: str = Field(title="last_name", max_length=100)
    username: str = Field(title="username", min_length=4)
    email: str = Field(title="E-mail", max_length=20)


class User(InputUser):
    id: int


class InputItem(BaseModel):
    name: str = Field(title="Name", max_length=50)
    price: float = Field(title="Price", gt=0, le=100000)
    quan: int = Field(title="Quantity", ge=0)
    description: str = Field(default=None, title="Description", max_length=1000)


class Item(InputItem):
    id: int


class InputOrder(BaseModel):
    user_id: int
    item_id: int
    quantity: int
    status: bool


class Order(BaseModel):
    id: int
    user: User
    item: Item
    quantity: int
    status: bool

