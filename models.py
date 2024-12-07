from sqlalchemy import Column, Integer, String, ForeignKey  
from sqlalchemy.orm import relationship, declarative_base  

Base = declarative_base()  

class Author(Base):  
    __tablename__ = 'authors'  
    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, nullable=False)  
    books = relationship('Book', back_populates='author')  

class Genre(Base):  
    __tablename__ = 'genres'  
    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, nullable=False)  
    books = relationship('Book', back_populates='genre')  

class Book(Base):  
    __tablename__ = 'books'  
    id = Column(Integer, primary_key=True, index=True)  
    title = Column(String, nullable=False)  
    author_id = Column(Integer, ForeignKey('authors.id'))  
    genre_id = Column(Integer, ForeignKey('genres.id'))  
    author = relationship('Author', back_populates='books')  
    genre = relationship('Genre', back_populates='books')  
