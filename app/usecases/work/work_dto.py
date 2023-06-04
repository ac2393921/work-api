from datetime import datetime

from pydantic import BaseModel


class WorkDTO(BaseModel):
    id: str
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
