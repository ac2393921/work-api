from pydantic import BaseConfig, BaseModel


class Entity(BaseModel):
    class Config(BaseConfig):
        validate_assignment = True
        frozen = False
