from database import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin

from schemas.task import Task as TaskSchema


class Task(Base, TimestampMixin):
    __tablename__ = 'tasks'

    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    title = Column(String(256), nullable=False)

    # リレーション設定
    user_id = Column(
        UUIDType(binary=False),
        ForeignKey('users.uuid'),
        nullable=True
    )
    user = relationship(
        'User',
        back_populates='tasks'
    )

    def to_read_model(self) -> TaskSchema:
        return TaskSchema(
            uuid=self.uuid,
            title=self.title,
        )
