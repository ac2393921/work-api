from pydantic import BaseModel


class CreateWorkInputPort(BaseModel):
    title: str
    description: str
