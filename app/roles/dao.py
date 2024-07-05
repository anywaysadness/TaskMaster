from app.dao.base import BaseDAO
from core.models import Role


class RoleDAO(BaseDAO):
    model = Role
