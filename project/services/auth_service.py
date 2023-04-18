import calendar
import datetime
import jwt
from flask import current_app
from flask_restx import abort

from project.dao import UsersDAO
from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import compose_passwords


class AuthsService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_user(self, mail: str) -> User:
        print(self, mail)
        if user := self.dao.get_by_email(mail):
            return user
        raise ItemNotFound(f'User with email={mail} not exists.')

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=current_app.config["SECRET_KEY"], algorithms=['HS256'])
        mail = data.get("email")

        return self.generate_tokens(mail, None, is_refresh=True)

    def generate_tokens(self, mail, password, is_refresh=False):

        user = self.get_user(mail)

        if user is None:
            raise abort(404)

        if is_refresh:
            data = {
                "email": user.email,
                "name": user.name
            }

            # 30 minutes for access_token
            min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            data["exp"] = calendar.timegm(min30.timetuple())
            access_token = jwt.encode(data, current_app.config["SECRET_KEY"], algorithm='HS256')

            # 130 days for refresh_token
            days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
            data["exp"] = calendar.timegm(days130.timetuple())
            refresh_token = jwt.encode(data, current_app.config["SECRET_KEY"], algorithm='HS256')

            return {
                "access_token": access_token,
                "refresh_token": refresh_token
            }

        if not is_refresh:
            if compose_passwords(user.password, password):
                data = {
                    "email": user.email,
                    "name": user.name
                }

                # 30 minutes for access_token
                min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                data["exp"] = calendar.timegm(min30.timetuple())
                access_token = jwt.encode(data, current_app.config["SECRET_KEY"], algorithm='HS256')

                # 130 days for refresh_token
                days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
                data["exp"] = calendar.timegm(days130.timetuple())
                refresh_token = jwt.encode(data, current_app.config["SECRET_KEY"], algorithm='HS256')

                return {
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }
        abort(400)

