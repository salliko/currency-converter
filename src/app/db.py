"""Модуль базы данных."""

import os

from databases import Database

from sqlalchemy import (
    Column,
    Float,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)


DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

currencies = Table(
    'Currencies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('char_code', String(3)),
    Column('num_code', Integer),
    Column('nominal', Integer),
    Column('name', String(50)),
    Column('value', Float),
)


database = Database(DATABASE_URL)
