from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
import inject

from schemas.task import Task as TaskSchema
from ddd.usecase.task_usecase import TaskQueryUseCase
from ddd.usecase.task_queryservice import TaskQueryService
from ddd.infrastructure.queryservice.task_queryservice import TaskQueryServiceImpl

router = APIRouter()

def configure_inject(db: Session):
    def inject_config(binder):
        binder.bind(TaskQueryService, TaskQueryServiceImpl(db))

    inject.clear_and_configure(inject_config)

@router.get('/', response_model=List[TaskSchema])
async def get_tasks(db: Session = Depends(get_db)):
    configure_inject(db)
    usecase = TaskQueryUseCase()
    tasks = usecase.get_tasks()
    return tasks

@router.get('/{task_id}', response_model=TaskSchema)
async def get_task(task_id: UUID, db: Session = Depends(get_db)):
    configure_inject(db)
    usecase = TaskQueryUseCase()
    task = usecase.get_task_by_id(task_id=task_id)
    return task
