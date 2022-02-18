from dataclasses import dataclass
from datetime import datetime
from random import randint


@dataclass
class ConnectionMock:
    url: str
    connection_time: datetime

    def start(self):
        print(f"Connection to {self.url} established")


class DbMock:

    @staticmethod
    def add_user(name: str):
        pass

    @staticmethod
    def connect(url: str):
        if not url:
            raise ConnectionError(f"url is not defined!")
        if isinstance(url, int):
            raise TypeError()
        return ConnectionMock(url=url, connection_time=datetime.utcnow())


class RequestMock:

    @staticmethod
    def get(url: str):
        return {
            "id": randint(1111111, 9999999),
            "name": "Get Request Mock",
            "url": url,
            "time_zone": "Etc/UTC",
            "updated_at": datetime.utcnow()
        }

    @staticmethod
    def post(url: str, data: str):
        return (True, url, data)

    @staticmethod
    def delete(url: str):
        return (True, url)
