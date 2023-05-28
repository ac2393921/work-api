from pydantic import BaseModel

from app.domain.entities.work import Work


class FetchWorkOutputPort(BaseModel):
    id: str
    title: str
