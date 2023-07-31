from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from typing import List

from app.server.models.todo import (
    Todo,
    TodoItem,
    TodoItems
)

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory="app/templates/")

@todo_router.get("/start")
async def start(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request
    })

@todo_router.post("/", status_code=201)
async def add_todo(request: Request, todo:Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })

@todo_router.get("/", response_model=List[TodoItems])
async def retrieve_todo(request : Request):
    try:
        return templates.TemplateResponse("todo.html", {
            "request": request,
            "todos": todo_list
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail="Todo is empty")

@todo_router.get("/{id}")
async def retrieve_single_todo(request: Request, id:int = Path(..., title="The ID of the Todo to retrieve")):
    try:
        for todo in todo_list:
            if todo.id == id:
                single_todo = todo
        return templates.TemplateResponse("todo.html", {
            "request": request,
            "todo": todo
        })
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with the ID doesnt exist!!!")

@todo_router.put("/{id}", response_model=TodoItem)
async def update_todo(todo_data: TodoItem, id:int = Path(..., title="The ID of Todo to be Updated")) -> dict:
    try:
        for todo in todo_list:
            if todo.id == id:
                todo.item = todo_data.item
            return {"response": "Updated the Todo Successfully!"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with the ID doesnt exist!!!")

@todo_router.delete("/{id}")
async def delete_single_todo(id:int) -> dict:
    try:
        for index in range(len(todo_list)):
            todo = todo_list[index]
            if todo.id == id:
                todo_list.pop(index)
                return {"response": "Todo deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist.")

@todo_router.delete("/")
async def delete_all() -> dict:
    todo_list.clear()
    return {"response": "Todos deleted successfully."}
