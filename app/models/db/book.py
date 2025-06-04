from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models.db.book_category import book_category
from app.models.db.base import Base

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    publication_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    
    # Relation avec l'auteur
    author = relationship("Author", back_populates="books")
    categories = relationship("Category", secondary=book_category, back_populates="books")
    