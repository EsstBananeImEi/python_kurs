import random
import string


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.id = "".join(random.choices(string.ascii_lowercase, k=10))
        self._status = "logged out"

    def set_status(self, status: str) -> None:
        self._status = status

    def get_status(self) -> str:
        return self._status


class Verificator_Email:
    def __init__(self) -> None:
        self._verified = False
        self._verification_code: str = ""

    def generate_verification_code(self) -> None:
        self._verification_code = "".join(
            random.choices(string.ascii_letters + string.digits + "!@#$%^&*()", k=10)
        )

    def get_verification_code(self) -> str:
        return self._verification_code

    def verify(self):
        verification_code = input("Enter Verification Code from Email: ")
        self._verified = verification_code == self._verification_code

    def is_verified(self) -> bool:
        return self._verified


class LoginProcessor:
    def login(self, user: User) -> None:
        verificator = Verificator_Email()
        verificator.generate_verification_code()
        verificator.verify()
        if not verificator.is_verified():
            raise Exception("Verification Failed")
        print(f"User: {user.name} \n" "ID: {user.id} \n" "Loggin ID: {user.id}")
        user.set_status("logged in")


# if __name__ == "__main__":
#     user = User("Melanie")
#     processor = LoginProcessor()
#     processor.login(user)

"""
Coverage generieren: 
    > coverage run ***_test.py
    > coverage html
"""
