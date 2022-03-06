from fastapi import APIRouter, HTTPException
from sqlalchemy import func

from ..db import database, currencies

router = APIRouter()


@router.get("/convert/{source}/{dest}/{value}")
async def convert(source: str, dest: str, value: float):
    stmt = currencies.select().where(func.lower(currencies.c.char_code) == func.lower(source))
    src = await database.fetch_one(stmt)
    if not src:
        raise HTTPException(status_code=404, detail=f"source '{source}' not found")

    stmt = currencies.select().where(func.lower(currencies.c.char_code) == func.lower(dest))
    dst = await database.fetch_one(stmt)
    if not dst:
        raise HTTPException(status_code=404, detail=f"dest '{dest}' not found")

    helf = value / src['value']
    result = round(helf * dst['value'], 4)

    return {"value": result}
