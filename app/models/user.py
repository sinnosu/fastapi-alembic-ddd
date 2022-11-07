from database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import sqlalchemy_utils
from uuid import uuid4
from .mixins import TimestampMixin

from schemas.user import User as UserSchema, UserTask as UserTaskSchema

class User(Base, TimestampMixin):
    __tablename__ = 'users'

    uuid = Column(sqlalchemy_utils.types.uuid.UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    email = Column(String(255), nullable=False, unique=True)
    username = Column(String(255), nullable=False)
    user_type = Column(Integer, nullable=False, default=3, doc="user type(1:system_admin, 2:admin, 3:normal")
    status = Column(Integer, nullable=False, default=1, doc="status(1:enabled, 2:disabled, 255:delete")
    password_enc = Column(String(255))

    # リレーション設定
    tasks = relationship(
        'Task',
        back_populates='user'
    )

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            uuid=self.uuid,
            username=self.username
        )

    def to_read_model_with_task(self) -> UserTaskSchema:
        return UserTaskSchema(
            uuid=self.uuid,
            username=self.username,
            tasks=self.tasks
        )
