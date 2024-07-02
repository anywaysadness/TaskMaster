from pydantic import BaseModel, ConfigDict


class STag(BaseModel):
    """
     Схема pydantic для Tags
     """
    id: int
    tag_name: str

    model_config = ConfigDict(from_attributes=True)
