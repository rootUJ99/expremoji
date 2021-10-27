from fastapi import APIRouter, Body, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .model import TaskModel

api  = APIRouter()

@api.get('/')
async def start_api():
    return {
        'start': 'hello world'
    }


@api.post("/", response_description="Add new task")
async def create_task(request: Request, task: TaskModel = Body(...)):
    task = jsonable_encoder(task)
    new_task = await request.app.mongodb["tasks"].insert_one(task)
    created_task = await request.app.mongodb["tasks"].find_one(
        {"_id": new_task.inserted_id}
    )
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_task)