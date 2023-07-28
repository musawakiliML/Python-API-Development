from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []

@todo_router.get("/start")
async def start() -> dict:
    return {"message": "Start Your Day With a Rich Todo List..."}

@todo_router.post("/todo")
async def add_todo(todo:dict) -> dict:
    todo_list.append(todo)
    return {"message":"Todo Successfully Added!"}

@todo_router.get("/todo")
async def retrieve_todo() -> dict:
    return {"response": todo_list}