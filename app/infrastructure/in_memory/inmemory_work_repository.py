from typing import List, Optional

from app.domain.entities.work import Work, WorkId
from app.domain.repositories.i_work_repository import IWorkRepository

in_memory_works = [
    {
        "id": "af58ace7-ab08-4256-89fe-2bef912bdf9d",
        "title": "Work 1",
        "description": "Work 1 description",
        "created_at": "2021-01-01T00:00:00Z",
        "updated_at": "2021-01-01T00:00:00Z",
    },
    {
        "id": "2111a70a-3b2d-4117-810e-269d713353a3",
        "title": "Work 2",
        "description": "Work 2 description",
        "created_at": "2021-01-01T00:00:00Z",
        "updated_at": "2021-01-01T00:00:00Z",
    },
    {
        "id": "b07f7f5a-e0eb-4a12-bab4-13950ef120b8",
        "title": "Work 3",
        "description": "Work 3 description",
        "created_at": "2021-01-01T00:00:00Z",
        "updated_at": "2021-01-01T00:00:00Z",
    },
]


class InMemoryWorkRepository(IWorkRepository):
    def find(self, work_id: str) -> Optional[Work]:
        work = None
        for work_data in in_memory_works:
            if work_data["id"] == work_id:
                work = Work(
                    id=WorkId(id=work_data["id"]),
                    title=work_data["title"],
                    description=work_data["description"],
                    created_at=work_data["created_at"],
                    updated_at=work_data["updated_at"],
                )
        return work

    def fetch_works(self) -> List[Work]:
        works = list()
        for work in in_memory_works:
            works.append(
                Work(
                    id=WorkId(id=work["id"]),
                    title=work["title"],
                    description=work["description"],
                    created_at=work["created_at"],
                    updated_at=work["updated_at"],
                )
            )

        return works

    def save(self, work: Work) -> None:
        in_memory_works.append(work.dict())

    def update(self, work: Optional[Work]) -> None:
        if not work:
            raise ValueError("Work not found")

        for i, work_data in enumerate(in_memory_works):
            if work_data["id"] == work.id.id:
                in_memory_works[i] = work.dict()
