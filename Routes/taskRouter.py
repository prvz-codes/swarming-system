from pydantic import BaseModel
from fastapi import APIRouter
from Core.dependencies import  missionControl


router = APIRouter()


class Task(BaseModel):
    x: int
    y: int
    task: str



@router.post("/tasks")
def add_tasks(task: Task):
    missionControl.performMissions(task.x, task.y, task.task)
    return {"message": "Task added"}