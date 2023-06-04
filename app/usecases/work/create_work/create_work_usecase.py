from abc import ABC, abstractmethod

from app.usecases.work.create_work.create_work_input_port import CreateWorkInputPort
from app.usecases.work.create_work.create_work_output_port import CreateWorkOutputPort


class CreateWorkUsecase(ABC):
    @abstractmethod
    def handle(self, input: CreateWorkInputPort) -> CreateWorkOutputPort:
        raise NotImplementedError
