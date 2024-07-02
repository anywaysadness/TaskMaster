from fastapi import APIRouter
from app.roles import SRole
from app.roles import RoleDAO

router = APIRouter(
    prefix="/roles",
    tags=["Роли"],
)


@router.get("/")
async def get_all_roles() -> list[SRole]:
    """

    :return: Все роли
    """
    return await RoleDAO.find_all()


@router.get("/{role_id}/")
async def get_role_by_id(role_id: int) -> SRole | None:
    """

    :return: Роль по id
    """
    return await RoleDAO.find_by_id(role_id)

