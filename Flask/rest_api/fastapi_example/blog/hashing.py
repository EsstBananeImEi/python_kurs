from uuid import uuid4

from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashPassword():
    @staticmethod
    def bcrypt_hash_password(password: str):
        return password_context.hash(password+uuid4().hex)
