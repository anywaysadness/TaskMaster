from fastapi import Request, HTTPException, Depends, status
from jose import jwt, JWTError
from core.config import settings
from datetime import datetime
from app.users.dao import UserDAO
from core.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from core.db_helper import db_helper


def get_token(request: Request):
    token = request.cookies.get("auth_access_token")
    if not token:
        raise HTTPException(401)
    return token


async def get_current_user(
        token: str = Depends(get_token),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await UserDAO.find_by_id(int(user_id), session=session)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user


def get_current_admin_user(user: User = Depends(get_current_user)):
    if user.back_roles.id != 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Недостаточно прав")
    return user
