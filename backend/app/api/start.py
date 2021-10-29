from fastapi import APIRouter, Body, Request, status, WebSocket
from fastapi import responses
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

@api.post('/test/{id}', response_description="delete the task")
async def remove_task(request: Request, id: str):
    print(id)
    deleted_task = await request.app.mongodb["tasks"].delete_one({'_id': id})
    if deleted_task.deleted_count:
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={
            'message': 'task has been deleted'
        })
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={
        'message': 'nothing to delete over here'
    })

@api.websocket('/ws')
async def testing_with_sockets(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f'this is the text {data}')
