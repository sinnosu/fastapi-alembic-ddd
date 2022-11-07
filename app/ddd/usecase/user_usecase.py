from uuid import UUID
from typing import List, Optional
import inject

from schemas.user import \
    User as UserSchema, UserTask as UserTaskSchema

from .user_queryservice import UserQueryService

class UserQueryUseCase:
    """UserQueryUseCase implements a query usecases related User entity."""

    def __init__(self):
        pass

    @inject.autoparams()
    def get_users(
            self,
            query_service: UserQueryService
    ) -> List[UserSchema]:
        try:
            users = query_service.find_all()
        except:
            raise

        return users

    @inject.autoparams()
    def get_user_task_by_id(
            self,
            user_id: UUID,
            query_service: UserQueryService
    ) -> Optional[UserTaskSchema]:
        try:
            user_tasks = query_service.find_task_by_id(user_id)
            if user_tasks is None:
                raise UserNotFoundError
        except:
            raise

        return user_tasks

