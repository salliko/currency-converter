from fastapi import APIRouter
from ..db import database, currencies


router = APIRouter()


@router.get("/rates/{char_code}")
async def rates(char_code: str):
    
    query = f"select * from currencies where lower(char_code) != lower('{char_code}')"
    response = await database.fetch_all(query)
    return response
    # return {
    #     "rates": [
    #         {
    #             "char_code": "AUD",
    #             "num_code": 36,
    #             "nominal": 1,
    #             "name": "Австралийский доллар",
    #             "value": 52.5603
    #         }
    #     ]
    # }
