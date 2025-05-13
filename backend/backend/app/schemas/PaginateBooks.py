from pydantic import BaseModel
from schemas.Book import Book

class PaginateBooks(BaseModel):
    data:list[Book] = []
    page:int = None
    totalPage:int = None