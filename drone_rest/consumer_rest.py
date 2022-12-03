from fastapi import FastAPI
from pydantic import BaseModel
from producer import proceed_to_deliver

app = FastAPI()


class Payload(BaseModel):
    details: dict


@app.post("/command")
def send_command_to_bus(payload: Payload):
    details = dict()
    proceed_to_deliver(None, payload.details)
