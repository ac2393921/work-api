from fastapi import FastAPI

from app.infrastructure.inmemory_work_repository import InMemoryWorkRepository
from app.usecases.get_work_usecase import GetWorkUsecase

app = FastAPI()


@app.get("/")
def get_works():
    usecase = GetWorkUsecase(repository=InMemoryWorkRepository())
    response = usecase.handle()
    return response
