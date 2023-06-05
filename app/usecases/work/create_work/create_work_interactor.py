import uuid
from datetime import datetime

from app.domain.entities.work import Work
from app.domain.repositories.i_work_repository import IWorkRepository
from app.domain.value_objects.work_id import WorkId
from app.usecases.work.create_work.create_work_input_port import CreateWorkInputPort
from app.usecases.work.create_work.create_work_output_port import (
    CreateWorkOutputPort,
    WorkDTO,
)
from app.usecases.work.create_work.create_work_usecase import CreateWorkUsecase


class CreateWorkInteractor(CreateWorkUsecase):
    def __init__(self, repository: IWorkRepository) -> None:
        self._repository = repository

    def handle(self, input: CreateWorkInputPort) -> CreateWorkOutputPort:
        work = Work(
            id=WorkId(id=str(uuid.uuid4())),
            title=input.title,
            description=input.description,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self._repository.save(work)
        return CreateWorkOutputPort(work=WorkDTO(**work.dict()))
