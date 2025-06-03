from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.db import book_category
from app.models.db.base import Base

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    
    livres = relationship("Livre", secondary=book_category, back_populates="categories"
    )