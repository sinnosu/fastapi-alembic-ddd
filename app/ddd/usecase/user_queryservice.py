from abc import ABC, abstractmethod
from typing import List, Optional

from schemas.user import User as UserSchema, UserTask as UserTaskSchema

class UserQueryService(ABC):
    """UserRepository defines a repository interface for User entity."""

    @abstractmethod
    def find_all(self) -> List[UserSchema]:
        pass

    @abstractmethod
    def find_task_by_id(self, id: str) -> Optional[UserTaskSchema]:
        pass

