from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.work import Work


class IWorkRepository(ABC):
    @abstractmethod
    def find(self, work_id: str) -> Work:
        return NotImplementedError()

    @abstractmethod
    def fetch_works(self) -> List[Work]:
        return NotImplementedError()

    @abstractmethod
    def save(self, work: Work) -> None:
        return NotImplementedError()

    @abstractmethod
    def update(self, work: Work, title: str, description: str) -> None:
        return NotImplementedError()
