from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.infrastructure.in_memory.inmemory_work_repository import InMemoryWorkRepository
from app.usecases.work.create_work.create_work_input_port import CreateWorkInputPort
from app.usecases.work.create_work.create_work_interactor import CreateWorkInteractor
from app.usecases.work.create_work.create_work_output_port import CreateWorkOutputPort
from app.usecases.work.fetch_work.fetch_work_input_port import FetchWorkInputPort
from app.usecases.work.fetch_work.fetch_work_interactor import FetchWorkInteractor
from app.usecases.work.fetch_work.fetch_work_output_port import FetchWorkOutputPort
from app.usecases.work.fetch_works.fetch_works_interactor import FetchWorksInteractor
from app.usecases.work.fetch_works.fetch_works_output_port import FetchWorksOutputPort
from app.usecases.work.update_work.update_work_input_port import UpdateWorkInputPort
from app.usecases.work.update_work.update_work_interactor import UpdateWorkInteractor
from app.usecases.work.update_work.update_work_output_port import UpdateWorkOutputPort

router = APIRouter(
    prefix="/works",
    tags=["works"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=FetchWorksOutputPort)
def get_works() -> JSONResponse:
    usecase = FetchWorksInteractor(repository=InMemoryWorkRepository())
    output = usecase.handle()
    return JSONResponse(
        content=jsonable_encoder(output),
    )


@router.get("/{work_id}", response_model=FetchWorkOutputPort)
def get_work(
    params: FetchWorkInputPort = Depends(FetchWorkInputPort),
) -> JSONResponse:
    usecase = FetchWorkInteractor(repository=InMemoryWorkRepository())
    output = usecase.handle(params)
    return JSONResponse(
        content=jsonable_encoder(output),
    )


@router.post(
    "/", response_model=CreateWorkOutputPort, status_code=status.HTTP_201_CREATED
)
def create_work(
    work: CreateWorkInputPort,
) -> JSONResponse:
    usecase = CreateWorkInteractor(repository=InMemoryWorkRepository())
    output = usecase.handle(work)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(output),
        headers={"Location": f"/works/{output.work.id}"},
    )


@router.put(
    "/", response_model=UpdateWorkOutputPort, status_code=status.HTTP_201_CREATED
)
def update_work(
    work: UpdateWorkInputPort,
) -> JSONResponse:
    usecase = UpdateWorkInteractor(repository=InMemoryWorkRepository())
    output = usecase.handle(work)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(output),
        headers={"Location": f"/works/{output.work.id}"},
    )
