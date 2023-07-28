from fastapi import APIRouter, Path

from app.server.models.todo import (
    Todo,
    Item
)

todo_router = APIRouter()

todo_list = []

@todo_router.get("/start")
async def start() -> dict:
    return {"message": "Start Your Day With a Rich Todo List..."}

@todo_router.post("/")
async def add_todo(todo:Todo) -> dict:
    todo_list.append(todo)
    return {"message":"Todo Successfully Added!"}

@todo_router.get("/")
async def retrieve_todo() -> dict:
    return {"response": todo_list}

@todo_router.get("/{id}")
async def retrieve_single_todo(id:int = Path(..., title="The ID of the Todo to retrieve")):
    
    for todo in todo_list:
        if todo.id == id:
            single_todo = todo

    return {"response":single_todo}