from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": {
                    "item":"Example Item!",
                    "status":"pending"
                }
            }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        json_Schema_extra = {
            "example": {
                "item":"Updated item!"
            }
        }