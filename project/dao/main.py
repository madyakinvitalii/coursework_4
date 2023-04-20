from typing import Optional

from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def create(self, user_d):
        ent = User(**user_d)
        self._db_session.add(ent)
        self._db_session.commit()
        return ent

    def update(self, user_d, user):
        user.name = user_d.get("name")
        user.surname = user_d.get("surname")
        user.favorite_genre = user_d.get("favorite_genre")

        self._db_session.add(user)
        self._db_session.commit()

    def change_pwd(self, new_password, user):
        user.password = new_password

        self._db_session.add(user)
        self._db_session.commit()
