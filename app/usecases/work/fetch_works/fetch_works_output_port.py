from typing import List

from pydantic import BaseModel

from app.usecases.work.work_dto import WorkDTO


class FetchWorksOutputPort(BaseModel):
    works: List[WorkDTO]
