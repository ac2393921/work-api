from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.work import Work


class IWorkRepository(ABC):
    @abstractmethod
    def fetch_works(self) -> List[Work]:
        return NotImplementedError()
