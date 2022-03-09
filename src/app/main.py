from fastapi import FastAPI

from .api import convert, rates
from .db import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()


@app.on_event('startup')
async def startup():
    """Функция срабатывает при запуске сервера."""
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    """Функция срабатывает при остановке сервера."""
    await database.disconnect()


app.include_router(rates.router)
app.include_router(convert.router)
