import jwt
from flask import current_app, abort

from project.dao import UsersDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_password_hash
from project.tools.security import compose_passwords

class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def create(self, user_d) -> User:
        user_d["password"] = generate_password_hash(user_d["password"])
        return self.dao.create(user_d)

    def get_user_by_mail(self, mail: str) -> User:
        if user := self.dao.get_by_email(mail):
            return user
        raise ItemNotFound(f'User with email={mail} not exists.')

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=current_app.config["SECRET_KEY"], algorithms=['HS256'])
        mail = data.get("email")

        return self.get_user_by_mail(mail)

    def update(self, user_d, user):
        self.dao.update(user_d, user)
        return self.dao

    def change_pwd(self, passwords, user):
        if compose_passwords(user.password, passwords["password_1"]):
            new_password = generate_password_hash(passwords["password_2"])
            self.dao.change_pwd(new_password, user)
            return self.dao
        else:
            abort(400)

