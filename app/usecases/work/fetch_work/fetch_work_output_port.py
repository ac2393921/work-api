from datetime import datetime

from pydantic import BaseModel

from app.usecases.work.work_dto import WorkDTO


class FetchWorkOutputPort(BaseModel):
    work: WorkDTO

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
