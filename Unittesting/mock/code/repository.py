from typing import TypeVar

from Unittesting.mock.code.base_repository import BaseRepository


class Repository(BaseRepository):

    def __init__(self, connection_str: str) -> None:
        super(Repository, self).__init__(connection_str)

    def _connect_db(self) -> None:
        self._connection = None

    def _disconnect_db(self) -> None:
        self._close_connection()

    def _close_connection(self) -> None:
        self._connection.close()

    def get_data(self, query) -> object:
        cursor = self._connection.cursor()
        cursor.execute(query)
        return cursor
