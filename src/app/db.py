import os

from sqlalchemy import (
    create_engine,
    MetaData,
    Integer,
    Column,
    String,
    Float,
    Table
)

from databases import Database


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

currencies = Table(
    "Currencies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("char_code", String(3)),
    Column("num_code", Integer),
    Column("nominal", Integer),
    Column("name", String(50)),
    Column("value", Float)
)


database = Database(DATABASE_URL)