from fastapi import APIRouter

router = APIRouter()


@router.get("/convert/{source}/{dest}/{value}")
async def convert():
    return {"value": 551.88315}
