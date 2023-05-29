from pydantic import BaseModel


class PositionId(BaseModel):
    screening_id: int
