from fastapi import Query, HTTPException

from src import schemas
from src.books_db import books


def get_books(
        offset: int = Query(default=0, ge=0, include_in_schema=False),
        limit: int = Query(default=0, ge=0, include_in_schema=False),
        search: str = Query(default="", include_in_schema=False),
) -> schemas.Books:
    if (offset + limit) == 0:
        top_index = len(books)
    else:
        top_index = offset + limit
    paginated_books = books[offset:top_index]
    selected_books = [
        book for book in paginated_books if
        search.lower() in book["title"].lower() or
        search.lower() in book["author"].lower() or
        search.lower() in book["publisher"].lower()
    ]
    return schemas.Books(
        books=[schemas.Book(**book) for book in selected_books]
    )
