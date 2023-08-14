import datetime

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

DATABASE_URL = "sqlite:///fincontrol.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

# Реестр
reestr = sqlalchemy.Table(
    "reests",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("code", sqlalchemy.String(5)),
    sqlalchemy.Column("operation_id", sqlalchemy.ForeignKey('operation.id'), nullable=False),
    sqlalchemy.Column("worker", sqlalchemy.ForeignKey('worker.id'), nullable=False),
    sqlalchemy.Column("control_action", sqlalchemy.ForeignKey('control_action.id'), nullable=False),
    sqlalchemy.Column("method", sqlalchemy.ForeignKey('method.id'), nullable=False),

)


# Процессы
process = sqlalchemy.Table(
    "process",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128)),

)


# Операции
operation = sqlalchemy.Table(
    "operation",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128)),
    sqlalchemy.Column("process_id", sqlalchemy.ForeignKey('process.id'), nullable=False),

)


# должность работника
employ_position = sqlalchemy.Table(
    "employ_position",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128)),

)

# работник
worker = sqlalchemy.Table(
    "worker",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128)),
    sqlalchemy.Column("surname", sqlalchemy.String(128)),
    sqlalchemy.Column("employ_position", sqlalchemy.ForeignKey('employ_position.id'), nullable=False),
)


# конрольное действие
control_action = sqlalchemy.Table(
    "control_action",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128)),

)

# метод котроля
method = sqlalchemy.Table(
    "method",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128)),

)
# Справка о нарушении
certificate_of_violations = sqlalchemy.Table(
    "certificate_of_violations",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("date", sqlalchemy.Date, default=datetime.datetime.utcnow),
    sqlalchemy.Column("worker", sqlalchemy.ForeignKey('worker.id'), nullable=False),

)

# Строка в справке о нарушениях
violation = sqlalchemy.Table(
    "violation",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("certificate_of_violations", sqlalchemy.ForeignKey('certificate_of_violations.id'), nullable=False),
    sqlalchemy.Column("core_reestr", sqlalchemy.ForeignKey('reestr.id'), nullable=False),
    sqlalchemy.Column("title", sqlalchemy.String(128)),
    sqlalchemy.Column("employ_position", sqlalchemy.ForeignKey('employ_position.id'), nullable=False),
    sqlalchemy.Column("worker", sqlalchemy.ForeignKey('worker.id'), nullable=False),
    sqlalchemy.Column("amount", sqlalchemy.Float),

)

# Журнал
journal = sqlalchemy.Table(
    "journal",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("date", sqlalchemy.Date, default=datetime.datetime.utcnow),
    sqlalchemy.Column("violation", sqlalchemy.ForeignKey('violation.id'), nullable=False),
    sqlalchemy.Column("measures", sqlalchemy.String(128)),

)



# Только для SQLite
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# для всех остальных
# engine = sqlalchemy.create_engine(DATABASE_URL)

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f'user{i}', email=f'mail{i}@mail.ru')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}


# @app.post("/users/", response_model=User)
# async def create_user(user: UserIn):
#     # query = users.insert().values(name=user.name, email=user.email)
#     query = users.insert().values(**user.dict())
#     last_record_id = await database.execute(query)
#     return {**user.dict(), "id": last_record_id}
#
#
# @app.get("/users/", response_model=List[User])
# async def read_users():
#     query = users.select()
#     return await database.fetch_all(query)
#
#
# @app.get("/users/{user_id}", response_model=User)
# async def read_user(user_id: int):
#     query = users.select().where(users.c.id == user_id)
#     return await database.fetch_one(query)
#
#
# @app.put("/users/{user_id}", response_model=User)
# async def update_user(user_id: int, new_user: UserIn):
#     query = users.update().where(users.c.id == user_id).values(**new_user.dict())
#     await database.execute(query)
#     return {**new_user.dict(), "id": user_id}
#
#
# @app.delete("/users/{user_id}")
# async def delete_user(user_id: int):
#     query = users.delete().where(users.c.id == user_id)
#     await database.execute(query)
#     return {'message': 'User deleted'}
#
#



