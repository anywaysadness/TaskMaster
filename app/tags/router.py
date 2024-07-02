from fastapi import APIRouter
from app.tags import STag
from app.tags import TagDAO

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
