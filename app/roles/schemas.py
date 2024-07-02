from pydantic import BaseModel, ConfigDict


class SRole(BaseModel):
    """
         Схема pydantic для Role
         """
    id: int
    role_name: str

    model_config = ConfigDict(from_attributes=True)
