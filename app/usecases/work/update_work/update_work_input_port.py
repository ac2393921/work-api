from pydantic import BaseModel


class UpdateWorkInputPort(BaseModel):
    id: str
    title: str
    description: str
