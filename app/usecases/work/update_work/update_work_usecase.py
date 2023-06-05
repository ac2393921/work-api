from abc import ABC, abstractmethod

from app.usecases.work.update_work.update_work_input_port import UpdateWorkInputPort
from app.usecases.work.update_work.update_work_output_port import UpdateWorkOutputPort


class UpdateWorkUsecase(ABC):
    @abstractmethod
    def handle(self, input: UpdateWorkInputPort) -> UpdateWorkOutputPort:
        raise NotImplementedError
