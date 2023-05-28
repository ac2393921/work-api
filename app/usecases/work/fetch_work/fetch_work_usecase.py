from app.domain.entities.work import Work
from app.domain.repositories.i_work_repository import IWorkRepository
from app.usecases.work.fetch_work.fetch_work_input_port import FetchWorkInputPort


class FetchWorkUsecase:
    def __init__(self, repository: IWorkRepository) -> None:
        self._repository = repository

    def handle(self, input: FetchWorkInputPort) -> Work:
        work_id = input.work_id
        work = self._repository.find(work_id)
        return work
