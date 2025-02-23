from fastapi import HTTPException, APIRouter, Depends
from fastapi.responses import JSONResponse

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


@router.post("", response_model=schemas.Book,
             summary="Create book",
             responses={201: {"description": "Book created successfully"}}
             )
def post_book(book: schemas.Book = Depends(utils.create_book)):
    """
    Create book
    """
    return JSONResponse(status_code=201, content=book)


@router.get("/{book_id}", response_model=schemas.Book, summary="Get book")
def get_book(book: dict = Depends(utils.get_book)):
    """
    Get book by id.\n
    """
    return book


@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, updated_book: schemas.Book):
    for i, book in enumerate(src.books_db.books):
        if book.get("book_id") == book_id:
            src.books_db.books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(src.books_db.books):
        if book.get("book_id") == book_id:
            del src.books_db.books[i]
            return {"message": "schemas.Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
