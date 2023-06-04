from pydantic import BaseModel


class ScreemingId(BaseModel):
    screening_id: int
