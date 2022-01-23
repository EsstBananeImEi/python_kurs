from dataclasses import dataclass
from datetime import datetime, timezone
from mailbox import FormatError
from random import randint


@dataclass
class ConnectionMock:
    url: str
    connection_time: datetime

    def start(self):
        print(f"Connection to {self.url} established")


class DbMock:

    @staticmethod
    def add_user(name):
        pass

    @staticmethod
    def complete_user_profile(name, client_name, plan):
        print(f"User {name} Created")

    @staticmethod
    def connect(url):
        if not url:
            raise ConnectionError(f"url is not defined!")
        if isinstance(url, int):
            raise TypeError()
        return ConnectionMock(url=url, connection_time=datetime.utcnow())


class RequestMock:

    @staticmethod
    def get(url):
        return {
            "id": randint(1111111, 9999999),
            "name": "Get Request Mock",
            "url": url,
            "time_zone": "Etc/UTC",
            "updated_at": datetime.utcnow()
        }

    @staticmethod
    def post(url, data):
        return (True, url, data)

    @staticmethod
    def delete(url):
        return (True, url)
