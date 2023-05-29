from datetime import datetime
from enum import Enum
from typing import List, Optinal

from pydantic import BaseModel

from app.domain.values.position_id import PositionId
from app.domain.values.screeming_id import ScreemingId


class ScreeningStatus(Enum):
    IN_PROGRESS = True
    ADOPTED = False
    REJECTED = False


class Interview(BaseModel):
    phase: int
    date_time: datetime


class Interviews:
    def __init__(self, value: Optinal[List[Interview]]):
        self._interviews = value

    def add_interview(self, interview_datetime: datetime):
        new_interview = Interview(
            phase=len(self._interviews) + 1,
            date_time=interview_datetime,
        )
        return Interviews(self._interviews.append(new_interview))

    @classmethod
    def empty():
        return Interviews([])


class Applicant(BaseModel):
    applicant_id: int


class Screening:
    def __init__(
        self,
        screening_id: ScreemingId,
        position_id: PositionId,
        status: ScreeningStatus,
        applicant: Applicant,
        apply_date_time: datetime,
    ):
        self._screening_id = screening_id
        self._position_id = position_id
        self._status = status
        self._interviews = Interviews.empty()
        self._applicant = applicant
        self._apply_date_time = apply_date_time
