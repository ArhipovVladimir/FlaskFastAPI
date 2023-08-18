import databases
# from sqlalchemy import Column, String, Integer, MetaData, Table, DateTime, create_engine, Numeric, ForeignKey
import sqlalchemy
from datetime import datetime
from settings import settings

db = databases.Database(settings.DATABASE_URL)
metadata = sqlalchemy.MetaData()

users_db = sqlalchemy.Table("users",
                            metadata,
                            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column("first_name", sqlalchemy.String(100)),
                            sqlalchemy.Column("last_name", sqlalchemy.String(100)),
                            sqlalchemy.Column("username", sqlalchemy.String(8)),
                            sqlalchemy.Column("email", sqlalchemy.String(20)),
                            # Column("created_on", DateTime(), default=datetime.now),
                            # Column("updated_on", DateTime(), default=datetime.now, onupdate=datetime.now)
                            )

items_db = sqlalchemy.Table("items",
                            metadata,
                            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column("name", sqlalchemy.String(50)),
                            sqlalchemy.Column("price", sqlalchemy.Numeric(10, 2)),
                            sqlalchemy.Column("quan", sqlalchemy.Integer),
                            sqlalchemy.Column("description", sqlalchemy.String(100), nullable=False),
                            )
#
orders_db = sqlalchemy.Table("order",
                             metadata,
                             sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column("user_id", sqlalchemy.ForeignKey('users.id')),
                             # sqlalchemy.Column("date_placed", sqlalchemy.DateTime(), default=datetime.now),
                             sqlalchemy.Column("item_id", sqlalchemy.ForeignKey('items.id')),
                             sqlalchemy.Column("quantity", sqlalchemy.Integer),
                             sqlalchemy.Column("status", sqlalchemy.Boolean, default=True)
                             )
#
#
# order_line_db = Table("order_line",
#                       metadata,
#                       Column("id", Integer, primary_key=True),
#                       Column("order_id", ForeignKey('order_db.id')),
#                       Column("item_id", ForeignKey('item_db.id')),
#                       Column("quantity", Integer)
#                       )

engine = sqlalchemy.create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)
