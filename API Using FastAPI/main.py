from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()

# main page


@app.get('/')
async def root():
    return {'message': 'Hello World!'}

# post item


@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict

# put item


@app.put('/items/{item_id}')
async def create_item_id(item_id: int, item: Item):
    return {'item_id': item_id, **item.dict()}


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
    '''Read user Id'''
    return {'user_id': user_id}
