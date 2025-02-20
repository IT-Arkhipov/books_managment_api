from pydantic import BaseModel


class Book(BaseModel):
    book_id: str
    title: str
    author: str
    year: int


class Books(BaseModel):
    books: list[Book]
