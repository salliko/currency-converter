from fastapi import FastAPI

app = FastAPI()


@app.get("/rates/{char_code}")
async def rates(char_code: str):
    return {
        "rates": [
            {
                "char_code": "AUD",
                "num_code": 36,
                "nominal": 1,
                "name": "Австралийский доллар",
                "value": 52.5603
            }
        ]
    }


@app.get("/convert/{source}/{dest}/{value}")
async def convert():
    return {"value": 551.88315}
