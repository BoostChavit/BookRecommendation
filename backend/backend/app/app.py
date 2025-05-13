from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import routes
from contextlib import asynccontextmanager
import joblib
from dotenv import load_dotenv
import os

from models.book import Base
from database import engine
from service.books_recommendation import BookRecommender

@asynccontextmanager
async def lifespan(app):
    try:
        Base.metadata.create_all(bind=engine)
        tfidf_vectorizer = joblib.load("service/tfidf_vectorizer.pkl")
        app.state.tfidf_vectorizer = BookRecommender(tfidf_vectorizer)
    except Exception as e:
        print(e)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(routes.router)

load_dotenv()
origins = [
    os.getenv('FRONTEND_URL')
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)