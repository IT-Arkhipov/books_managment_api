from typing import Optional

from fastapi import HTTPException, APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.responses import Response
from starlette import status

from src import utils, schemas

router = APIRouter(prefix="/books", tags=["books"])


@router.get(
    "",
    response_model=schemas.Books,
    summary="Get books",
    status_code=status.HTTP_200_OK,
)
def get_books(books: schemas.Books = Depends(utils.get_books)) -> schemas.Books:
    """
    Get all books.\n
    Hidden parameters:\n
    - offset [int] - books list offset\n
    - description [int] - number of books per query
    - search [str] - filter books list by searched entry in title, author or publisher
    """
    return books


@router.post(
    "",
    response_model=schemas.Book,
    summary="Create book",
    responses={status.HTTP_201_CREATED: {"description": "Book created successfully"}},
    status_code=status.HTTP_201_CREATED,
)
def post_book(book: dict = Depends(utils.create_book)):
    """
    Create book
    """
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=book)


@router.get(
    "/{book_id}",
    response_model=schemas.Book,
    summary="Get book",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Book not found"}
    },
    status_code=status.HTTP_200_OK,
)
def get_book(book: schemas.Book = Depends(utils.get_book)) -> Optional[schemas.Book]:
    """
    Get a book by its id.\n
    """
    return book


@router.put(
    "/{book_id}",
    response_model=schemas.Book,
    summary="Update book",
    responses={
        status.HTTP_200_OK: {"description": "Book updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Book not found"},
    },
    status_code=status.HTTP_200_OK,
)
def update_book(book=Depends(utils.update_book)) -> Optional[schemas.Book]:
    return book


@router.delete(
    "/{book_id}",
    summary="Delete book",
    dependencies=[Depends(utils.delete_book)],
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Book deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Book not found"},
    },
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_book():
    return Response(status_code=status.HTTP_204_NO_CONTENT)
