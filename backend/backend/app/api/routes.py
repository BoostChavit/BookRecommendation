from fastapi import APIRouter, HTTPException, Depends, Request
from schemas.Book import Book
from sqlalchemy.orm import Session

from database import get_db
from models.book import BookModel
from schemas.Book import Book
from schemas.PaginateBooks import PaginateBooks

router = APIRouter()

@router.get("/books", response_model=PaginateBooks)
def read_books(
    page: int,
    offset: int,
    category: str='',
    db: Session = Depends(get_db)
):
    if page <= 0:
        return PaginateBooks()

    current = (page - 1) * offset
    query = None

    if category:
        query = db.query(BookModel).filter(BookModel.category == category)
    else:
        query = db.query(BookModel)

    total = query.count()

    if current > total:
        return PaginateBooks()
    
    books = query.order_by(BookModel.id.asc()).offset(current).limit(offset).all()
    totalPage = (total + offset - 1) // offset
    return PaginateBooks(
        data=books,
        page=page,
        totalPage=totalPage
    )

@router.get("/book/{id}", response_model=Book)
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(BookModel.category).order_by(BookModel.category.asc()).distinct().all()
    return [c[0] for c in categories]

@router.get("/recommend", response_model=list[Book])
def get_recommend(id: int, request: Request, db: Session = Depends(get_db)):
    if not hasattr(request.app.state, 'tfidf_vectorizer'):
        raise HTTPException(
            status_code=503,
            detail="Recommendation service is not ready"
        )
    recommender = request.app.state.tfidf_vectorizer
    books_id = recommender.recommend(id)
    books = []
    for book_id in books_id:
        books.append(db.query(BookModel).filter(BookModel.id == book_id).first())
    return books