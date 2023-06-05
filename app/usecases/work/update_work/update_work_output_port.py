from datetime import datetime

from pydantic import BaseModel

from app.usecases.work.work_dto import WorkDTO


class UpdateWorkOutputPort(BaseModel):
    work: WorkDTO

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
