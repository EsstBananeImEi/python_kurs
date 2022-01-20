from datetime import datetime, timezone
from random import randint


class DbMock:

    @staticmethod
    def add_user(name):
        pass

    @staticmethod
    def complete_user_profile(name, client_name, plan):
        print(f"User {name} Created")


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
