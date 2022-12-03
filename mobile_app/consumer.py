from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import producer

app = FastAPI()


class Drone_info(BaseModel):
    payload: dict


class Drone_control(BaseModel):
    commad_name: str
    pin: int


@app.post("/")
def get_drone_info(drone_info: Drone_info):
    return ""


@app.get("/command")
def send_command(drone_control: Drone_control):
    producer.authorize(drone_control.pin)
    details = {
        "command_name": drone_control.commad_name,
        "deliver_to": "fly_control"
    }
    producer.send_command_to_drone(details)
