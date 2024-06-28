from fastapi import APIRouter
from app.database_connect import async_session_maker
from app.roles.models import Role
from sqlalchemy import select

router = APIRouter(
    prefix="/roles",
    tags=["Роли"],
)


@router.get("")
async def get_all_roles():
    """

    :return: Все роли
    """
    async with async_session_maker() as session:
        query = select(Role).order_by("role_id")   # SELECT * FROM roles
        result = await session.execute(query)
        return result.scalars().all()

