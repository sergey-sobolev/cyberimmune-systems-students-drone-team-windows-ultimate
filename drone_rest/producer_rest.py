import httpx


def call_external_api(payload: dict):
    if (payload["deliver_to"] == "mobile_app"):
        url = "http://localhost:8000"
    elif (payload["deliver_to"] == "control_center"):
        url = "http://localhost:8001"
    response = httpx.post(url, json=payload)
    if (response.text != None):
        return response.text
