from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.roles import SRole
from app.roles import RoleDAO
from core.db_helper import db_helper

router = APIRouter(
    prefix="/roles",
    tags=["Роли"],
)


@router.get("/", response_model=list[SRole])
async def get_all_roles(
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await RoleDAO.find_all(session=session)


@router.get("/{role_id}/", response_model=SRole)
async def get_role_by_id(
        role_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await RoleDAO.find_by_id(role_id, session=session)
