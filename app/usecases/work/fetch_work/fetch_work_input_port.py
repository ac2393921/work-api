from pydantic import BaseModel


class FetchWorkInputPort(BaseModel):
    work_id: str
