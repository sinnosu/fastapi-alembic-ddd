from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm.exc import NoResultFound

from models.user import User as UserModel
from schemas.user import User as UserSchema, UserTask as UserTaskSchema

from ddd.usecase.user_queryservice import UserQueryService
from ddd.infrastructure.queryservice.base_queryservice import BaseQueryService

class UserQueryServiceImpl(BaseQueryService, UserQueryService):
    """UserDbRepository implements CRUD operations related User entity using SQLAlchemy."""

    def find_all(self) -> List[UserSchema]:
        try:
            results = self.db.query(UserModel).all()
        except NoResultFound:
            return None
        except:
            raise

        return list(map(lambda r: r.to_read_model(), results))

    def find_task_by_id(self, user_id: UUID) -> Optional[UserTaskSchema]:
        try:
            result = self.db.query(UserModel).get(user_id)
        except NoResultFound:
            return None
        except:
            raise

        return result.to_read_model_with_task()

