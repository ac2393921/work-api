from typing import List

from app.domain.entities.work import Work
from app.domain.repositories.i_work_repository import IWorkRepository

WORKS = [
    {
        "id": "1",
        "title": "Work 1",
        "description": "Work 1 description",
        "created_at": "2021-01-01T00:00:00Z",
        "updated_at": "2021-01-01T00:00:00Z",
    },
    {
        "id": "2",
        "title": "Work 2",
        "description": "Work 2 description",
        "created_at": "2021-01-01T00:00:00Z",
        "updated_at": "2021-01-01T00:00:00Z",
    },
    {
        "id": "3",
        "title": "Work 3",
        "description": "Work 3 description",
        "created_at": "2021-01-01T00:00:00Z",
        "updated_at": "2021-01-01T00:00:00Z",
    },
]


class InMemoryWorkRepository(IWorkRepository):
    def fetch_works(self) -> List[Work]:
        works = list()
        for work in WORKS:
            works.append(Work(**work))

        return works
