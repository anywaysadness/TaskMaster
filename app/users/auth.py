from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from pydantic import EmailStr
from app.users.dao import UserDAO
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """
    Функция для хеширования переданного пароля
    :param password: Переданный пароль
    :return: Хешированый пароль
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    """
    Функция для сравнения переданного пароля с хэшированным паролем из БД
    :param plain_password: Переданный пароль
    :param hashed_password: Хешированый пароль из БД
    :return: True | False
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """
    Функция для создания токена
    :param data:
    :return:
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(user_email: EmailStr, user_pass: str):
    user = await UserDAO.find_one_or_none(user_email=user_email)
    if not user and not verify_password(user_pass, user.user_pass):
        return None
    return user
