class BaseRepository(object):
    def __init__(self, connection_str="") -> None:
        self._connection_str = connection_str

    def __eq__(self, other: object) -> bool:
        if other is not None:
            if other._connection_str == self._connection_str \
                    and other._connection == self._connection:
                return True
        return False

    def __enter__(self):
        self._connect_db()
        return self

    def __exit__(self, *args) -> None:
        self._disconnect_db()

    def _connect_db(self) -> None:
        NotImplementedError

    def _disconnect_db(self) -> None:
        NotImplementedError
