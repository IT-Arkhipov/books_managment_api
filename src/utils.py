from fastapi import Query, HTTPException

from src import schemas
from src.books_db import books


def get_books(
        offset: int = Query(default=0, ge=0),
        limit: int = Query(default=5, ge=1, le=10)) -> schemas.Books:
    paginated_books = books[offset:offset+limit]
    return schemas.Books(
        books=[schemas.Book(**book) for book in paginated_books]
    )
