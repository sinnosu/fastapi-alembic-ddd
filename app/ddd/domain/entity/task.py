from typing import Optional

class Task:
    """Task represents your collection of tasks as an entity."""

    def __init__(
            self,
            uuid: str,
            title: str,
            created_at: Optional[int] = None,
            updated_at: Optional[int] = None,
    ):
        self.uuid: str = uuid
        self.title: str = title
        self.created_at: Optional[int] = created_at
        self.updated_at: Optional[int] = updated_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Task):
            return self.id == o.id

        return False
