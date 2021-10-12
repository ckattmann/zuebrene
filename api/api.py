import time
import json
import random
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

class User(BaseModel):
    username: str
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

fake_users_db = {
    "ckattmann": {
        "username": "ckattmann",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

def fake_hash_password(password: str):
    return "fakehashed" + password



def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(user_dict)

def decode_token(token):
    return User(username=token+"fake")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = decode_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={'WWW-Authenticate': 'Bearer'}
        )
    return user

@app.get('/users/me')
async def read_user_me(current_user: User=Depends(get_current_user)):
    return current_user

@app.get('/items')
async def read_items(token: str = Depends(oauth2_scheme)):
    return {'token': token, 'bobert': 'hubert'}

@app.post('/api/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    return {'access_token': user.username, 'token_type': 'bearer'}




@app.get("/api/sites")
def get_sites():
    with open("sites.json") as f:
        sites = json.load(f)
    return sites


# @app.get("/api/livedata")
# def get_livedata():
#     with open("sites.json") as f:
#         sites = json.load(f)
#     for sitename in sites.keys():
#         if sitename == "site6":
#             sites[sitename]["pd_value"] = random.gauss(15, 2)
#             sites[sitename]["temperature"] = random.gauss(85, 10)
#         elif sitename == "site9":
#             sites[sitename]["pd_value"] = random.gauss(10, 2)
#             sites[sitename]["temperature"] = random.gauss(85, 10)
#         else:
#             sites[sitename]["pd_value"] = max(0, random.gauss(5, 2))
#             sites[sitename]["temperature"] = random.gauss(65, 20)
#     return sites


# @app.get("/api/historicData")
# def get_historic_data():
#     data = [random.gauss(15, 2) for x in range(100)]
#     return data


# @app.get("/api/betterHistoricData")
# def get_better_historic_data():
#     ten_minutes_ago = int(time.time() - 60 * 10)
#     timedata = list(range(ten_minutes_ago, ten_minutes_ago + 600, 1))
#     data = [random.gauss(65, 20) for x in range(600)]
#     return [timedata, data]
