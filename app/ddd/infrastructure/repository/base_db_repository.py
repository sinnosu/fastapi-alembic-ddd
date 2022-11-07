from sqlalchemy.orm.session import Session


class BaseDbRepository:
    def __init__(self, db: Session) -> None:
        self.db = db