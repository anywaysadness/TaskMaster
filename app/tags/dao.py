from core.models import Tag
from app.dao.base import BaseDAO


class TagDAO(BaseDAO):
    model = Tag
