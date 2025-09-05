from pydantic import BaseModel


class TodoCreate(BaseModel):
    text: str

class TodoUpdate(BaseModel):
    text: str
    completed: bool