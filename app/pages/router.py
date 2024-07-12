from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.users.router import get_all_users, show_all_tasks_with_all_users, show_tasks_by_user_id
from app.tasks.router import get_task_by_id
from app.users.dao import UserDAO
from sqlalchemy.ext.asyncio import AsyncSession
from core.db_helper import db_helper

router = APIRouter(
    prefix="/pages",
    tags=["Frontend"]
)


templates = Jinja2Templates(directory="app/templates")


@router.get("/tasks/{user_id}")
async def get_task_by_id(
        request: Request,
        user_id: int,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    user = await show_tasks_by_user_id(user_id=user_id, session=session)
    return templates.TemplateResponse(
        name="card_task.html",
        context={"request": request, "user": user}
    )


@router.get("/users")
async def get_users_page(
        request: Request,
        users=Depends(show_all_tasks_with_all_users),

):
    return templates.TemplateResponse(
        name="card_user.html",
        context={"request": request, "users": users}
    )


@router.get("/login")
async def login(
        request: Request,
):
    return templates.TemplateResponse(
        name="login.html",
        context={"request": request}
    )


