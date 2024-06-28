from pydantic import BaseModel, ConfigDict
from datetime import datetime


class SUser(BaseModel):
    """
    Схема pydantic для User
    """
    id: int
    user_first_name: str
    user_second_name: str
    user_middle_name: str
    user_email: str
    user_pass: str
    user_position: str | None
    user_date_creation: datetime
    role_id: int
    image_id: int | None

    model_config = ConfigDict(from_attributes=True)
