from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
import inject

from schemas.user import \
    User as UserSchema, UserTask as UserTaskSchema

from ddd.usecase.user_usecase import UserQueryUseCase
from ddd.usecase.user_queryservice import UserQueryService
from ddd.infrastructure.queryservice.user_queryservice import UserQueryServiceImpl

router = APIRouter()

def configure_inject(db: Session):
    def inject_config(binder):
        binder.bind(UserQueryService, UserQueryServiceImpl(db))

    inject.clear_and_configure(inject_config)


@router.get('/', response_model=List[UserSchema])
async def get_users(db: Session = Depends(get_db)):
    configure_inject(db)
    usecase = UserQueryUseCase()
    users = usecase.get_users()
    return users

@router.get('/{user_id}', response_model=UserTaskSchema)
async def get_user_task(user_id: UUID, db: Session = Depends(get_db)):
    configure_inject(db)
    usecase = UserQueryUseCase()
    user_tasks = usecase.get_user_task_by_id(user_id=user_id)

    return user_tasks
