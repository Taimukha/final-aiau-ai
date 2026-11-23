
import pytest

from src.book_tools import load_books, search_books, get_book_details


# Test 1: Check if books are loaded
def test_load_books():
    books = load_books()
    assert len(books) > 0


# Test 2: Search books by language
def test_search_books_by_language():
    results = search_books(language="English")

    assert len(results) == 2
    assert all(book["language"] == "English" for book in results)


# Test 3: Search books by genre
def test_search_books_by_genre():
    results = search_books(genre="Psychology & Self-development")

    assert len(results) == 3


# Test 4: Get book details by ID
def test_get_book_details():
    book = get_book_details(1)

    assert book is not None
    assert book["title"] == "Атом әдеттер"


# Test 5: Check non-existing book ID
def test_get_book_details_not_found():
    book = get_book_details(100)

    assert book is None


# Test 6: Reject unsupported language
def test_search_invalid_language():
    with pytest.raises(ValueError):
        search_books(language="Korean")


# Test 7: Reject unsupported genre
def test_search_invalid_genre():
    with pytest.raises(ValueError):
        search_books(genre="Horror")


# Test 8: Reject invalid input type
def test_search_invalid_input_type():
    with pytest.raises(ValueError):
        search_books(language=123)


# Test 9: Reject invalid book ID type
def test_get_book_details_invalid_id():
    with pytest.raises(ValueError):
        get_book_details("one")
