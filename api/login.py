import json
import random
import time

import influxdb
import simpleinflux as influx

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

app = FastAPI()

JWT_SECRET = "afkj239408sdhfpoqahwjeopfighasdkjfgh"

manager = LoginManager(JWT_SECRET, "/api/token")

INFLUX_CLIENT = influxdb.InfluxDBClient(database="zuebrene")

DB = {
    "users": {
        "ckattmann": {"name": "ckattmann", "password": "hunter2"},
        "mheckel": {"name": "mheckel", "password": "winterbach"},
        "lhoefer": {"name": "lhoefer", "password": "traubenuss"},
        "jhohlloch": {"name": "jhohlloch", "password": "knusperkeks"},
        "pfisterer": {"name": "pfisterer", "password": "dummyloop"},
        "dpassow": {"name": "dpassow", "password": "vollnuss"},
    }
}


@manager.user_loader()
def query_user(user_id: str):
    return DB["users"].get(user_id)


@app.post("/api/token")
def login(data: OAuth2PasswordRequestForm = Depends()):
    print(data.username)
    user = query_user(data.username)
    print(user)
    if not user:
        print(f"Unknown user {user}")
        raise InvalidCredentialsException
    elif data.password != user["password"]:
        print(f"Wrong password for user {user}:{data.password}")
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data={"sub": data.username})

    return {"token": access_token}


@app.get("/api/sites")
def get_sites():
    with open("sites.json") as f:
        sites = json.load(f)
    return sites


@app.get("/api/livedata")
def get_livedata(user=Depends(manager)):
    print(user)
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


@app.get("/api/sites2")
def get_sites2():
    measurements = [d["name"] for d in INFLUX_CLIENT.get_list_measurements()]
    return measurements

@app.get("/api/config")
def get_config():
    with open('config.json') as f:
        config = json.load(f)
    return config


@app.get("/api/livedata2")
def get_livedata2():
    measurements = get_sites2()

    livedata = {}

    for measurement in measurements:
        points = list(
            INFLUX_CLIENT.query(
                f"select * from {measurement} order by time desc limit 1", epoch="ms"
            ).get_points()
        )[0]
        livedata[measurement] = points

    print(livedata)
    return livedata
    # get_points()
    # return {}


@app.get("/api/historicData")
def get_historic_data():
    data = [random.gauss(15, 2) for x in range(100)]
    return data


@app.get("/api/betterHistoricData")
def get_better_historic_data(measurement: str, timeframe: str, aggregation: str):
    # ten_minutes_ago = int(time.time() - 60 * 10)
    # timedata = list(range(ten_minutes_ago, ten_minutes_ago + 600, 1))
    # data = [random.gauss(65, 20) for x in range(600)]
    # return [timedata, data]
    # print("===========")
    # print(influx.read_latest("client_0", db="zuebrene"))
    # print("===========")
    # data = influx.read_special_range("client_0", "today", db='zuebrene')
    if aggregation.lower() == 'none':
        aggregation = None
    data = influx.read_special_range(measurement, timeframe, aggregation=aggregation, db='zuebrene')
    return data


if __name__ == "__main__":
    # print(get_livedata2())
    print(get_better_historic_data())
