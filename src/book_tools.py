
import json
from pathlib import Path


VALID_LANGUAGES = ["Kazakh", "Russian", "English"]

VALID_GENRES = [
    "Psychology & Self-development",
    "Fiction",
    "Adventure & Fantasy",
    "Mystery & Detective"
]


def load_books():
    file_path = Path(__file__).parent.parent / "books.json"

    with open(file_path, "r", encoding="utf-8") as file:
        books = json.load(file)

    return books


def search_books(language=None, genre=None, query=None):

    # Validate input types
    if language is not None and not isinstance(language, str):
        raise ValueError("Language must be a string")

    if genre is not None and not isinstance(genre, str):
        raise ValueError("Genre must be a string")

    if query is not None and not isinstance(query, str):
        raise ValueError("Query must be a string")

    # Validate language
    if language and language not in VALID_LANGUAGES:
        raise ValueError(f"Unsupported language: {language}")

    # Validate genre
    if genre and genre not in VALID_GENRES:
        raise ValueError(f"Unsupported genre: {genre}")

    books = load_books()
    results = []

    for book in books:

        if language and book["language"].lower() != language.lower():
            continue

        if genre and book["genre"].lower() != genre.lower():
            continue

        if query:
            search_text = (
                book["title"] + " " +
                book["author"] + " " +
                book["description"] + " " +
                " ".join(book["topics"])
            ).lower()

            if query.lower() not in search_text:
                continue

        results.append(book)

    return results


def get_book_details(book_id):

    if not isinstance(book_id, int) or isinstance(book_id, bool):
        raise ValueError("Book ID must be an integer")

    books = load_books()

    for book in books:
        if book["id"] == book_id:
            return book

    return None
