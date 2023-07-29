from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        json_schema_extra = {
            "Example": {
                "id": 1,
                "Item":{
                    "item":"Example Item!",
                    "status":"pending"
                }
            }
        }