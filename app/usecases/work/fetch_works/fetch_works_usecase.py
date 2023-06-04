from abc import ABC, abstractmethod

from app.domain.repositories.i_work_repository import IWorkRepository
from app.usecases.work.fetch_works.fetch_works_output_port import FetchWorksOutputPort
from app.usecases.work.work_dto import WorkDTO


class FetchWorksUsecase(ABC):
    @abstractmethod
    def handle(self) -> FetchWorksOutputPort:
        raise NotImplementedError()
