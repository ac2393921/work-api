from app.domain.repositories.i_work_repository import IWorkRepository


class GetWorkUsecase:
    def __init__(self, repository: IWorkRepository) -> None:
        self._repository = repository

    def handle(self):
        works = self._repository.fetch_works()
        return works
