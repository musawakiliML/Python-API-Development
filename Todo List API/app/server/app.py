from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.server.routes.todo import router as TodoRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(TodoRouter, tags="Start Todo List")

@app.get("/")
async def welcome() -> dict:
    return {"message":"Welcome to my Todo List APIs"}