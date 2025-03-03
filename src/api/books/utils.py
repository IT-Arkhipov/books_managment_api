from fastapi import Query, HTTPException

from src.api.books import schemas
from src.data.books_db import books


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


def get_book(book_id: str) -> schemas.Book:
    for book in books:
        if book.get("book_id") == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


def create_book(new_book: schemas.Book) -> dict:
    for book in books:
        if book.get("book_id") == new_book.book_id:
            raise HTTPException(status_code=400, detail="Book already exists")

    appended_book = schemas.Book(
        book_id=new_book.book_id,
        title=new_book.title,
        author=new_book.author,
        year=new_book.year).model_dump()
    books.append(appended_book)
    return appended_book


def update_book(book_id: str, new_book: schemas.BookUpdate) -> schemas.Book:
    for book in books:
        if book.get("book_id") == book_id:
            books.remove(book)
            updated_book = new_book.model_dump()
            updated_book["book_id"] = book_id
            return schemas.Book(**create_book(schemas.Book(**updated_book)))
    raise HTTPException(status_code=404, detail="Book not found")


def delete_book(book_id: str):
    for book in books:
        if book.get("book_id") == book_id:
            books.remove(book)
            return None
    raise HTTPException(status_code=404, detail="Book not found")
