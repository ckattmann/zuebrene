from fastapi import FastAPI
import time
import json
import random


app = FastAPI()


@app.get("/api/sites")
def get_sites():
    with open("sites.json") as f:
        sites = json.load(f)
    return sites


@app.get("/api/livedata")
def get_livedata():
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
