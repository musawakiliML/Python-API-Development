from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# main page


@app.get('/')
async def root():
    return {'message': 'Hello World!'}

# get item id path


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}

# get current user path


@app.get('/users/me')
async def read_user_me():
    return {'user_id': "the current user"}

# get user by id


@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}
