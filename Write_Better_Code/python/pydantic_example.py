import json
import pydantic
from typing import Optional


class ISBN10FormatError(Exception):
    def __init__(self, isbn: str, message: str) -> None:
        self.message = message
        self.isbn = isbn
        super().__init__(message)


class ISBN10MissingError(Exception):
    def __init__(self, title: str, message: str) -> None:
        self.message = message
        self.title = title
        super().__init__(message)


class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn10_or_isbn13(cls, values: dict[str, str]):
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBN10MissingError(
                title=values['title'], message="Das Buch sollte entweder eine ISBN10 oder ISBN13 haben.")
        return values

    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, isbn: str):
        chars = [char for char in isbn if char in "0123456789xX"]
        if len(chars) != 10:
            raise ISBN10FormatError(
                isbn=isbn, message="ISBN10 muss 10 zahlen haben.")

        def char_to_int(char: str) -> int:
            if char in "xX":
                return 10
            return int(char)

        isbn_sum = sum((10 - index) * char_to_int(char)
                       for index, char in enumerate(chars))
        if isbn_sum % 11 != 0:
            raise ISBN10FormatError(
                isbn=isbn, message="Die Summe der ISBN10 zahlen muss durch 11 teilbar sein.")

    class Config:
        allow_mutation = False  # make book imutable
        anystr_lower = True  # make all strings lowercase


def main() -> None:
    with open('./Materialien/books.json') as book_file:
        data = json.load(book_file)
        books: list[Book] = [Book(**item) for item in data]
        print(books[0].author)


if __name__ == '__main__':
    main()
