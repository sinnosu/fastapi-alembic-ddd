from sqlalchemy.orm.session import Session


class BaseQueryService:
    def __init__(self, db: Session) -> None:
        self.db = db