from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime


class SUser(BaseModel):
    """
    Схема pydantic для User
    """
    id: int
    user_first_name: str
    user_second_name: str
    user_middle_name: str
    user_email: EmailStr
    user_pass: str
    user_position: str | None
    user_date_creation: datetime
    role_id: int | None
    image_id: int | None

    model_config = ConfigDict(from_attributes=True)


class SUserAuth(BaseModel):
    """
    Схема pydantic для аутентификации User
    """
    user_email: EmailStr
    user_pass: str

    model_config = ConfigDict(from_attributes=True)


class SUserRegister(BaseModel):
    """
    Схема pydantic для регистрации User
    """
    user_first_name: str
    user_second_name: str
    user_middle_name: str
    user_email: EmailStr
    user_pass: str

    model_config = ConfigDict(from_attributes=True)
