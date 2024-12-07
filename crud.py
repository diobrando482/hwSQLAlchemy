from sqlalchemy.future import select  
from sqlalchemy.ext.asyncio import AsyncSession  
from models import Author, Genre, Book  

async def add_author(session: AsyncSession, name: str):  
    author = Author(name=name)  
    session.add(author)  
    await session.commit()  
    await session.refresh(author)  
    return author  

async def add_genre(session: AsyncSession, name: str):  
    genre = Genre(name=name)  
    session.add(genre)  
    await session.commit()  
    await session.refresh(genre)  
    return genre  

async def add_book(session: AsyncSession, title: str, author_id: int, genre_id: int):  
    book = Book(title=title, author_id=author_id, genre_id=genre_id)  
    session.add(book)  
    await session.commit()  
    await session.refresh(book)  
    return book  

async def get_books(session: AsyncSession):  
    result = await session.execute(select(Book))  
    return result.scalars().all()  

async def get_book_by_id(session: AsyncSession, book_id: int):  
    result = await session.execute(select(Book).where(Book.id == book_id))  
    return result.scalars().first()  

async def delete_book(session: AsyncSession, book_id: int):  
    book = await get_book_by_id(session, book_id)  
    if book:  
        await session.delete(book)  
        await session.commit()  
    return book  
