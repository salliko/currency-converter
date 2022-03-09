"""Модуль convert."""

from app.db import currencies, database

from fastapi import APIRouter, HTTPException, status

from sqlalchemy import func


router = APIRouter()


@router.get('/convert/{source}/{dest}/{summa}')
async def convert(source: str, dest: str, summa: float):
    """Функция конвертирует данные."""
    stmt = currencies.select().where(
        func.lower(currencies.c.char_code) == func.lower(source),
    )
    src = await database.fetch_one(stmt)
    if not src:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='source "{0}" not found'.format({source}),
        )

    stmt = currencies.select().where(
        func.lower(currencies.c.char_code) == func.lower(dest),
    )
    dst = await database.fetch_one(stmt)
    if not dst:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='dest "{0}" not found'.format(dest),
        )

    helf = summa / src['value']
    return {'value': round(helf * dst['value'], 4)}
