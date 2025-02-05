from dataclasses import dataclass
import requests


@dataclass
class Book:
    description: str
    isbn: str
    title: str
    subtitle: str
    authors: list
    rating: float
    published: str
    thumbnails: list[dict]


def get_book_from_api(isbn: str) -> Book:
    url = f"https://book-monkey2-api.angular-buch.com/book/{isbn}"

    response = requests.get(url)
    if response.status_code == 200:
        return Book(**response.json())
    else:
        return Book(
            description="",
            isbn=isbn,
            title="",
            subtitle="",
            authors=[],
            rating=0.0,
            published="",
            thumbnails=[],
        )


def get_all_books_from_api():
    url = "https://book-monkey2-api.angular-buch.com/books/"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
