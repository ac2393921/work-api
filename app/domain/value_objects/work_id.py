from app.domain.value_objects.value_object import ValueObject


class WorkId(ValueObject):
    id: str

    def __str__(self) -> str:
        return self.id
