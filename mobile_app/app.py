import httpx
from pydantic import BaseModel
import json


pin_auth_url = "http://localhost:8003/pin-login"
drone_url = "http://localhost:8002/command"
max_attempts = 3


def send_command(command: str, jwt: str):
    try:
        return httpx.post(drone_url, json={"command": command, "jwt": jwt})
    except:
        return None


def authorize(pin: str):
    try:
        response = httpx.post(
            pin_auth_url, json={"pin": pin})
        if (response.status_code == 403):
            return None
        # ТУТ JWT и ключ
        return json.loads(response.text)
    except:
        return None


def main():
    attempts = 0
    auth = None

    while auth is None and attempts < max_attempts:
        pin = input("Enter PIN: ")
        auth = authorize(pin)
        if auth is None:
            print("Invalid PIN or server error!")
        attempts += 1

    if attempts >= max_attempts:
        print("Access denied")
        return

    print("Successfully authenticated")

    while True:
        command = input("Enter command: ")
        response = send_command(command, auth["jwt"])
        if response is None:
            print("Error while sendind command")
        elif response.status_code != 200:
            print("Command failed")
        else:
            print("Command succeed")


main()
