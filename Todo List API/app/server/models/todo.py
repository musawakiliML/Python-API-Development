from pydantic import BaseModel
from typing import List


# class Item(BaseModel):
#     item: str
#     status: str

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Item!"
            }
        }
        # json_schema_extra = {
        #     "example": {
        #         "id": 1,
        #         "item": {
        #             "item":"Example Item!",
        #             "status":"pending"
        #         }
        #     }
        # }

class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item":"Updated item!"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example Schema 1!"
                    },
                    {
                        "item": "Example Schema 2!"
                    }
                ]
            }
        }