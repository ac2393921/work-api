from abc import ABC, abstractmethod

from app.usecases.work.fetch_work.fetch_work_input_port import FetchWorkInputPort
from app.usecases.work.fetch_work.fetch_work_output_port import FetchWorkOutputPort


class FetchWorkUsecase(ABC):
    @abstractmethod
    def handle(self, input: FetchWorkInputPort) -> FetchWorkOutputPort:
        raise NotImplementedError
