from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime


class SUserBase(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SUser(SUserBase):
    """
    Схема pydantic для User
    """
    user_first_name: str
    user_second_name: str
    user_middle_name: str
    user_email: EmailStr
    user_pass: str
    user_position: str | None
    user_date_creation: datetime


class SUserResponse(BaseModel):
    user_first_name: str
    user_second_name: str
    user_middle_name: str
    user_email: EmailStr
    user_position: str | None

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


class SUserUpdate(BaseModel):
    user_first_name: str
    user_second_name: str
    user_middle_name: str
    user_position: str

    model_config = ConfigDict(from_attributes=True)


class SUserUpdatePartial(BaseModel):
    user_first_name: str | None = None
    user_second_name: str | None = None
    user_middle_name: str | None = None
    user_position: str | None = None

    model_config = ConfigDict(from_attributes=True)
