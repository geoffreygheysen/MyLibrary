from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.db.base import Base

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    
    # Un auteur peut avoir plusieurs livres (1-N)
    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")
    