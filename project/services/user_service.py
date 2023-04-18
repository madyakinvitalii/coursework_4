from project.dao import UsersDAO
from project.models import User
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def create(self, user_d) -> User:
        user_d["password"] = generate_password_hash(user_d["password"])
        return self.dao.create(user_d)
