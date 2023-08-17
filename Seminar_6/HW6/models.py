from pydantic import BaseModel, Field


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
    quantity: int = Field(title="Quantity", gt=0)
    description: str = Field(default=None, title="Description", max_length=1000)


class Item(InputItem):
    item_id: int


class InputOrder(BaseModel):
    user: int
    date: str = Field(title="Description", max_length=1000)
    date_placed: str
    item: int
    quantity: int = Field(title="Quantity", gt=0)


class Order(InputOrder):
    order_id: int
