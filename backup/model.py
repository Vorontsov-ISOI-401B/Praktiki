from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
            "examples": [{
                "id": 1,
                "item": "Example schema!"
            }]
        }