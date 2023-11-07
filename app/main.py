from typing import Union
from fastapi import FastAPI
from dj_weather_show.weather_show import get_weather
import time
import random

app = FastAPI()


def pick_presenter(members: list) -> str:
    """
    - https://github.com/Sam1000won/random_chocie/blob/1.0.0/src/project/choice.py
    """
    return random.choice(members)


@app.get("/whoau")
def whoau():
    """pick presenter
    - fork : https://github.com/Sam1000won/random_chocie/blob/1.0.0/src/project/choice.py
    Returns:
       json : team, presenter
    """
    team_i_five = ["심재호", "강민정", "김하현", "박수빈", "안인균"]
    team_dp = ["서형원", "탁정균", "한지웅", "오동균", "이태경", "백승아"]
    team_teamgun = ["이은총", "김범수", "김주한", "이승언", "신예랑"]

    teams = ["i-Five", "D.P", "teamgun"]
    teams = random.sample(teams, len(teams))

    return {
        "i-Five": pick_presenter(team_i_five),
        "D.P": pick_presenter(team_dp),
        "teamgun": pick_presenter(team_teamgun),
        "presentation order": "👉 ".join(teams)

    }


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
