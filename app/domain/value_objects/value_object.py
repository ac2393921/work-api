from pydantic import BaseConfig, BaseModel


class ValueObject(BaseModel):
    class Config(BaseConfig):
        validate_assignment = True
        frozen = True
