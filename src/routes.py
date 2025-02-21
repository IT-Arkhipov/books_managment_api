from fastapi import HTTPException, APIRouter, Depends

import src.books_db
from src import utils, schemas

router = APIRouter(prefix="/books")


@router.get("", response_model=schemas.Books, summary="Get books")
def get_books(books: list = Depends(utils.get_books)):
    """
    Get all books.\n
    Hidden parameters:\n
    - offset [int] - books list offset\n
    - description [int] - number of books per query
    - search [str] - filter books list by searched entry in title, author or publisher
    """
    return books


@router.post("", response_model=schemas.Book)
def create_book(book: schemas.Book):
    src.books_db.books.append(book)
    return book


@router.get("/{book_id}", response_model=schemas.Book)
def get_book(book_id: int):
    for book in src.books_db.books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="schemas.Book not found")


@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, updated_book: schemas.Book):
    for i, book in enumerate(src.books_db.books):
        if book.id == book_id:
            src.books_db.books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="schemas.Book not found")


@router.delete("/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(src.books_db.books):
        if book.id == book_id:
            del src.books_db.books[i]
            return {"message": "schemas.Book deleted"}
    raise HTTPException(status_code=404, detail="schemas.Book not found")
