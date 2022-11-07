from typing import Optional
from uuid import UUID
from sqlalchemy.orm.exc import NoResultFound

from models.task import Task as TaskModel
from schemas.task import Task as TaskSchema

from ddd.usecase.task_queryservice import TaskQueryService
from ddd.infrastructure.queryservice.base_queryservice import BaseQueryService

class TaskQueryServiceImpl(BaseQueryService, TaskQueryService):
    """TaskDbRepository implements CRUD operations related Task entity using SQLAlchemy."""

    def find_all(self) -> Optional[TaskSchema]:
        try:
            results = self.db.query(TaskModel).all()
        except NoResultFound:
            return None
        except:
            raise

        return list(map(lambda r: r.to_read_model(), results))

    def find_by_id(self, task_id: UUID) -> Optional[TaskSchema]:
        try:
            result = self.db.query(TaskModel).get(task_id)
        except NoResultFound:
            return None
        except:
            raise

        return result.to_read_model()

