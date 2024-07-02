from fastapi import APIRouter
from app.database_connect import async_session_maker
from app.tags.models import Tag
from sqlalchemy import select
from app.tags.schemas import STag
from app.tags.dao import TagDAO

router = APIRouter(
    prefix="/tags",
    tags=["Тэги"],
)


@router.get("/")
async def get_all_tags() -> list[STag]:
    """

    :return: Получить список всех тегов
    """
    return await TagDAO.find_all()


@router.get("/{tag_id}/")
async def get_tag_by_id(tag_id: int) -> STag | None:
    """

    :return: Получить тег по id
    """
    return await TagDAO.find_by_id(tag_id)
