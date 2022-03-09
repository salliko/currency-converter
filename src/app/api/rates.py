from typing import Optional

from fastapi import APIRouter, HTTPException, status

from sqlalchemy import asc, desc, func

from ..db import currencies, database

router = APIRouter()


@router.get('/rates/{char_code}')
async def rates(
    char_code: str,
    sort_by: Optional[str] = None,
    order_by: Optional[str] = None,
    search: Optional[str] = None,
):
    """Функция конвертирует валюты к валюте."""
    stmt = currencies.select().where(
        func.lower(currencies.c.char_code) == func.lower(char_code),
    )
    currency = await database.fetch_one(stmt)
    if not currency:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='char code not found',
        )

    if search:
        stmt = currencies.select().where(
            func.lower(currencies.c.char_code) == func.lower(search),
        )
    else:
        stmt = currencies.select().where(
            func.lower(currencies.c.char_code) != func.lower(char_code),
        )

    if sort_by and order_by:
        if sort_by in {'name', 'char_code', 'num_code'} and order_by in {'asc', 'desc'}:
            sort = asc(sort_by) if order_by == 'asc' else desc(sort_by)
            stmt = stmt.order_by(sort)

    response = await database.fetch_all(stmt)

    # TODO: реализовать логику конвертирования

    return response
