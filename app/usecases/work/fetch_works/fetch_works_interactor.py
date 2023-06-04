from app.domain.repositories.i_work_repository import IWorkRepository
from app.usecases.work.fetch_works.fetch_works_output_port import FetchWorksOutputPort
from app.usecases.work.fetch_works.fetch_works_usecase import FetchWorksUsecase
from app.usecases.work.work_dto import WorkDTO


class FetchWorksInteractor(FetchWorksUsecase):
    def __init__(self, repository: IWorkRepository) -> None:
        self._repository = repository

    def handle(self) -> FetchWorksOutputPort:
        works = self._repository.fetch_works()
        return FetchWorksOutputPort(
            works=[WorkDTO(**work.dict()) for work in works],
        )
