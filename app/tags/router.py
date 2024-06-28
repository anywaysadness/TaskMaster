from fastapi import APIRouter
from app.database_connect import async_session_maker
from app.tags.models import Tag
from sqlalchemy import select

router = APIRouter(
    prefix="/tags",
    tags=["Тэги"],
)


@router.get("")
async def get_all_tags():
    """

    :return: Все тэги
    """
    async with async_session_maker() as session:
        query = select(Tag).order_by("tag_id")   # SELECT * FROM tags
        result = await session.execute(query)
        return result.scalars().all()


@router.get("/{tag_id}")
async def get_tag_by_id():
    """

    :return: Тэг по id
    """
    pass
