import httpx


auth_url = "http://localhost:8003/login"
drone_url = "http://localhost:8002"
jwt = None


def send_command_to_drone(details: dict):
    if (jwt is None):
        raise Exception("Not authenticated")
    details["source"] = jwt
    httpx.post(drone_url, details)


def authorize(pin: str):
    response = httpx.post(
        auth_url, {"serviceName": "mobile_app", "password": pin})
    jwt = response.text
