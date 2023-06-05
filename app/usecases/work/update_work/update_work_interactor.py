from datetime import datetime

from app.domain.repositories.i_work_repository import IWorkRepository
from app.usecases.work.update_work.update_work_input_port import UpdateWorkInputPort
from app.usecases.work.update_work.update_work_output_port import (
    UpdateWorkOutputPort,
    WorkDTO,
)
from app.usecases.work.update_work.update_work_usecase import UpdateWorkUsecase


class UpdateWorkInteractor(UpdateWorkUsecase):
    def __init__(self, repository: IWorkRepository) -> None:
        self._repository = repository

    def handle(self, input: UpdateWorkInputPort) -> UpdateWorkOutputPort:
        work = self._repository.find(input.id)
        work.change_title(input.title)
        work.change_description(input.description)
        work.change_updated_at(datetime.now())
        self._repository.update(work)
        return UpdateWorkOutputPort(work=WorkDTO(**work.dict()))
