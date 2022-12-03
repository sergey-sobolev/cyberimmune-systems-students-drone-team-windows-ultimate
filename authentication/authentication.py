from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt

app = FastAPI()

services = {
    "drone": "drone",
    "mobile_app": "1234",
    "control_center": "control_center"
}

secret = "secret"


class Login(BaseModel):
    serviceName: str
    password: str


class PinLogin(BaseModel):
    pin: str


class JwtToken(BaseModel):
    token: str


class MobileResponse(BaseModel):
    jwt: str
    key: str = "{aes}123-klhgojehrjogsojsdjflvkjkbjd"


@app.post("/login")
def login(login: Login):
    if (services[login.serviceName] == login.password):
        return jwt.encode({"serviceName": login.serviceName}, secret, algorithm="HS256")
    else:
        return None


@app.post("/pin-login")
def pin_login(login: PinLogin):
    if (services["mobile_app"] == login.pin):
        token = jwt.encode({"serviceName": "mobile_app"},
                           secret, algorithm="HS256")
        response = MobileResponse(jwt=token)
        return response
    else:
        raise HTTPException(status_code=403, detail="Bad pin")


@app.get("/service/{token}")
def verify(token: str):
    try:
        response = jwt.decode(token, secret, algorithms=["HS256"])
    except:
        response = None
    return response
