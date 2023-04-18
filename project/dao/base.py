from typing import Generic, List, Optional, TypeVar

from flask import current_app
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import scoped_session
from werkzeug.exceptions import NotFound

from project.models import User
from project.setup.db.models import Base

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    __model__ = Base

    def __init__(self, db_session: scoped_session) -> None:
        self._db_session = db_session

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

    def get_by_id(self, pk: int) -> Optional[T]:
        return self._db_session.query(self.__model__).get(pk)

    def get_by_email(self, mail: str):
        return self._db_session.query(self.__model__).filter(self.__model__.email == mail).first_or_404()

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None) -> List[T]:
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if page is not None and status == 'new':
            stmt: BaseQuery = self._db_session.query(self.__model__).order_by(self.__model__.created)
            try:
                return stmt.paginate(page=page, per_page=self._items_per_page).items
            except NotFound:
                return []
        if status == 'new':
            stmt: BaseQuery = self._db_session.query(self.__model__).order_by(self.__model__.created)
            return stmt.all()
        if page:
            try:
                return stmt.paginate(page=page, per_page=self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

