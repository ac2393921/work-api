from app.domain.repositories.i_work_repository import IWorkRepository
from app.usecases.work.fetch_work.fetch_work_input_port import FetchWorkInputPort
from app.usecases.work.fetch_work.fetch_work_output_port import FetchWorkOutputPort
from app.usecases.work.fetch_work.fetch_work_usecase import FetchWorkUsecase
from app.usecases.work.work_dto import WorkDTO


class FetchWorkInteractor(FetchWorkUsecase):
    def __init__(self, repository: IWorkRepository) -> None:
        self._repository = repository

    def handle(self, input: FetchWorkInputPort) -> FetchWorkOutputPort:
        work = self._repository.find(input.work_id)
        return FetchWorkOutputPort(work=WorkDTO(**work.dict()))
