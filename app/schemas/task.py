from pydantic import BaseModel
from uuid import UUID


class Task(BaseModel):
    uuid: UUID
    title: str

    class Config:
        orm_mode = True