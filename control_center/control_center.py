from fastapi import FastAPI, HTTPException
import httpx
from task import Task, Coordinates

app = FastAPI()
auth_url = "http://localhost:8003/service"


tasks = {
    "default": Task("default", [Coordinates(0, 0, 0), Coordinates(5, 5, 5)], [Coordinates(5, 5, 5), Coordinates(6, 6, 6)])
}


@app.get("/task/{task_name}")
def get_task(task_name: str):
    return tasks[task_name]


@app.post("/task")
def create_task(task: Task):
    tasks[task.name] = task


def authorize(jwt: str):
    response = httpx.get(auth_url, json={"token": jwt})
    if (response is None):
        raise HTTPException(status_code=403, detail="Invalid token")
