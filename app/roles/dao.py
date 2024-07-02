from app.dao.base import BaseDAO
from app.roles.models import Role


class RoleDAO(BaseDAO):
    model = Role
