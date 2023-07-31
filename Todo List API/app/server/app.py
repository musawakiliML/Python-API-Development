from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.server.routes.todo import todo_router as TodoRouter
from app.server.routes.todo_updated import todo_router as TodoUpdatedRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def welcome() -> dict:
    return {"message":"Welcome to my Todo List APIs"}

app.include_router(TodoRouter, tags=["Start Todo List"], prefix="/todo")
app.include_router(TodoUpdatedRouter, tags=["Todo Application"], prefix="/todo_v1")