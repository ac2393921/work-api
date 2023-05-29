from fastapi import APIRouter

from app.infrastructure.inmemory_work_repository import InMemoryWorkRepository
from app.usecases.work.fetch_work.fetch_work_input_port import FetchWorkInputPort
from app.usecases.work.fetch_work.fetch_work_output_port import FetchWorkOutputPort
from app.usecases.work.fetch_work.fetch_work_usecase import FetchWorkUsecase
from app.usecases.work.fetch_works.fetch_works_usecase import FetchWorksUsecase

router = APIRouter(
    prefix="/works",
    tags=["works"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_works():
    usecase = FetchWorksUsecase(repository=InMemoryWorkRepository())
    response = usecase.handle()
    return response


@router.get("/{work_id}")
def get_work(work_id: str) -> FetchWorkOutputPort:
    input = FetchWorkInputPort(work_id=work_id)
    usecase = FetchWorkUsecase(repository=InMemoryWorkRepository())
    response = usecase.handle(input)
    return FetchWorkOutputPort(id=response.id, title=response.title)