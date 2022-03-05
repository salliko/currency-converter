from fastapi import FastAPI

from .api import rates, convert

app = FastAPI()

app.include_router(rates.router)
app.include_router(convert.router)
