from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.tags import STag
from app.tags import TagDAO
from core.db_helper import db_helper

router = APIRouter(
    prefix="/tags",
    tags=["Тэги"],
)


@router.get("/", response_model=list[STag])
async def get_all_tags(
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await TagDAO.find_all(session=session)


@router.get("/{tag_id}/", response_model=STag)
async def get_tag_by_id(
        tag_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    tag = await TagDAO.find_by_id(tag_id, session=session)
    if not tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return tag
