from uuid import UUID
from typing import List, Optional

import inject

from schemas.task import Task as TaskSchema
from .task_queryservice import TaskQueryService

class TaskQueryUseCase:
    """TaskQueryUseCase implements a query usecases related Task entity."""

    def __init__(self):
        pass

    @inject.autoparams()
    def get_tasks(
            self,
            query_service: TaskQueryService
    ) -> List[TaskSchema]:
        try:
            tasks = query_service.find_all()
        except:
            raise

        return tasks

    @inject.autoparams()
    def get_task_by_id(
            self,
            task_id: UUID,
            query_service: TaskQueryService
    ) -> Optional[TaskSchema]:
        try:
            task = query_service.find_by_id(task_id)
            if task is None:
                raise TaskNotFoundError
        except:
            raise

        return task

