from datetime import datetime
from typing import List
from pydantic import BaseModel
from uuid import UUID
from .task import Task


class User(BaseModel):
    uuid: UUID
    username: str
    # 返す必要のない値は記述しなければ
    # レスポンスから切り捨てられる
    # created_at: datetime
    # updated_at: datetime

    # リレーションを張っている場合は
    # 書かないとバリデーションエラーになる
    class Config:
        orm_mode = True


class UserTask(User):
    tasks: List[Task] = []