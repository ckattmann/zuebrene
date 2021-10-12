import json
import random
import time

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

app = FastAPI()

JWT_SECRET = 'afkj239408sdhfpoqahwjeopfighasdkjfgh'

manager = LoginManager(JWT_SECRET, '/api/token')

DB = {
    'users': {
        'ckattmann': {
            'name': 'ckattmann',
            'password': 'hunter2'
        }
    }
}

@manager.user_loader()
def query_user(user_id: str):
    return DB['users'].get(user_id)

@app.post('/api/token')
def login(data: OAuth2PasswordRequestForm = Depends()):
    user = query_user(data.username)
    print(user)
    if not user:
        raise InvalidCredentialsException
    elif data.password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data={'sub': data.username})

    return {'token':access_token}

@app.get("/api/sites")
def get_sites():
    with open("sites.json") as f:
        sites = json.load(f)
    return sites


@app.get("/api/livedata")
def get_livedata(user=Depends(manager)):
    with open("sites.json") as f:
        sites = json.load(f)
    for sitename in sites.keys():
        if sitename == "site6":
            sites[sitename]["pd_value"] = random.gauss(15, 2)
            sites[sitename]["temperature"] = random.gauss(85, 10)
        elif sitename == "site9":
            sites[sitename]["pd_value"] = random.gauss(10, 2)
            sites[sitename]["temperature"] = random.gauss(85, 10)
        else:
            sites[sitename]["pd_value"] = max(0, random.gauss(5, 2))
            sites[sitename]["temperature"] = random.gauss(65, 20)
    return sites

@app.get("/api/historicData")
def get_historic_data():
    data = [random.gauss(15, 2) for x in range(100)]
    return data

@app.get("/api/betterHistoricData")
def get_better_historic_data():
    ten_minutes_ago = int(time.time() - 60 * 10)
    timedata = list(range(ten_minutes_ago, ten_minutes_ago + 600, 1))
    data = [random.gauss(65, 20) for x in range(600)]
    return [timedata, data]

