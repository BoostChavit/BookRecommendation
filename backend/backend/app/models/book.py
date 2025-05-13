from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column("title", String)
    description = Column("description", String)
    author = Column("author", String)
    image_link = Column("image_link", String)
    category = Column("category", String)
    rating = Column("rating", Float)