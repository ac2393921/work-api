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
    def add(self, work: Work) -> None:
        return NotImplementedError()
