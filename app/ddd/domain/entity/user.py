from typing import Optional, List
from .task import Task

class User:
    """User represents your collection of users as an entity."""

    def __init__(
            self,
            uuid: str,
            email: str,
            username: str,
            user_type: str,
            status: str,
            created_at: Optional[int] = None,
            updated_at: Optional[int] = None,
            tasks: Optional[List[Task]] = None,

    ):
        self.uuid: str = uuid
        self.email: str = email
        self.username: str = username
        self.user_type: str = user_type
        self.status: str = status
        self.created_at: Optional[int] = created_at
        self.updated_at: Optional[int] = updated_at
        self.tasks: List[Task] = tasks

    def __eq__(self, o: object) -> bool:
        if isinstance(o, User):
            return self.id == o.id

        return False
