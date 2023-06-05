from datetime import datetime

from app.domain.entities.entity import Entity
from app.domain.value_objects.work_id import WorkId


class Work(Entity):
    id: WorkId
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            WorkId: str,
        }

    def dict(self, **kwargs):
        base_dict = super().dict(**kwargs)
        base_dict["id"] = self.id.id
        return base_dict

    def change_title(self, title: str) -> None:
        self.title = title

    def change_description(self, description: str) -> None:
        self.description = description

    def change_updated_at(self, updated_at: datetime) -> None:
        self.updated_at = updated_at
