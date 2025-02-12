from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/books")

books_db = []


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


@router.get("", response_model=List[Book])
def get_books():
    return books_db


@router.post("", response_model=Book)
def create_book(book: Book):
    books_db.append(book)
    return book


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            books_db[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[i]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
