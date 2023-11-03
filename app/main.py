from typing import Union
from fastapi import FastAPI
from dj_weather_show.weather_show import get_weather
import time

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/weather")
def read_root():
    """DJ weather"""
    location, weather_condition, temperature = get_weather()
    return {"location": location, "weather_condition": weather_condition, "temperature": temperature}


@app.get("/iambest/{limit:int}")
async def iambest(limit: int):
    start = time.time()
    sum: int = 0
    for i in range(limit):
        sum += i

    duration = time.time() - start

    if sum > 2**63 - 1:
        raise HTTPException(
            status_code=400, detail="Sum overflow."
        )

    return {"duration": duration, "limit": limit, "sum": sum}
