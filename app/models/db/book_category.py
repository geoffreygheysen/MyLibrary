from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models.db.base import Base

# Table d'association pour la relation N-N entre Livre et Categorie
book_category = Table(
    'book_category',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True)
)