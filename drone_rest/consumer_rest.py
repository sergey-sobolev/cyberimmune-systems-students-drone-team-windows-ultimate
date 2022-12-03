from producer import start_producer
from consumer import start_consumer
from multiprocessing import Queue
from configparser import ConfigParser
from argparse import ArgumentParser, FileType
from fastapi import FastAPI
from pydantic import BaseModel
from producer import proceed_to_deliver
import httpx
import threading

app = FastAPI()


class JwtToken(BaseModel):
    token: str


class Payload(BaseModel):
    command: str
    jwt: str


@app.post("/command")
def send_command_to_bus(payload: Payload):
    print("Got command")
    print(payload)
    details = dict()
    details["deliver_to"] = "fly_control"
    details["source"] = get_source(payload.jwt)
    details["command"] = payload.command
    proceed_to_deliver(None, details)


auth_url = "http://localhost:8003/service"


def get_source(jwt: str):
    response = httpx.get(auth_url + jwt)
    if (response is None):
        print(f"[error] authentication failed for {jwt}")
        return None
    return response.text


def start_rest(requests_queue):
    global _requests_queue
    _requests_queue = requests_queue
    threading.Thread(target=lambda: app.run(host="localhost",
                     port=8002, debug=True, use_reloader=False)).start()


if __name__ == "__main__":        # on running python app.py
    start_rest()
