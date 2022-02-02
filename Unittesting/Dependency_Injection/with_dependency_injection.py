import random
import string


class User:

    def __init__(self, name) -> None:
        self.name = name
        self.id = ''.join(random.choices(string.ascii_lowercase, k=10))
        self._status = 'logged out'

    def set_status(self, status) -> None:
        self._status = status

    def get_status(self) -> str:
        return self._status


class Verificator_Email:

    def __init__(self) -> None:
        self._verified = False
        self._verification_code = None

    def _generate_verification_code(self):
        self._verification_code = ''.join(random.choices(
            string.ascii_letters + string.digits + "!@#$%^&*()", k=10))

    def verify(self):
        verification_code = input("Enter Verification Code from Email: ")
        self._verified = verification_code == self._verification_code

    def is_verified(self) -> bool:
        return self._verified


class LoginProcessor:

    def __init__(self, verificator: Verificator_Email) -> None:
        self.verificator = verificator

    def login(self, user) -> None:
        self.verificator.verify()
        if not self.verificator.is_verified():
            raise Exception("Verification Failed")
        print(f"User: {user.name} \n"
              f"ID: {user.id} \n")
        user.set_status("logged in")


# if __name__ == "__main__":
#     user = User("Melanie")
#     verificator = Verificator_Email()
#     verificator._generate_verification_code()
#     processor = LoginProcessor(verificator)
#     processor.login(user)
