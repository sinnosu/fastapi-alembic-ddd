from fastapi import FastAPI, APIRouter
from ddd.presentation.user import router as user_router
from ddd.presentation.task import router as task_router

router = APIRouter()

# users
router.include_router(
    user_router,
    prefix='/users',
    tags=['users']
)

# tasks
router.include_router(
    task_router,
    prefix='/tasks',
    tags=['tasks']
)

app = FastAPI()
app.include_router(router)

