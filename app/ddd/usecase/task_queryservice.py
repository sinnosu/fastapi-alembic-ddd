from abc import ABC, abstractmethod
from typing import List, Optional

from schemas.task import Task as TaskSchema

class TaskQueryService(ABC):
    """TaskRepository defines a repository interface for Task entity."""

    @abstractmethod
    def find_all(self) -> List[TaskSchema]:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[TaskSchema]:
        pass

