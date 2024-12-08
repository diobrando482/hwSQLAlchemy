from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from db.models import Book, Author, Genre


async def add_author(session:AsyncSession,name:str):
    author = Author(name=name)
    session.add(author)
    await session.commit()
    return  author

async def add_genre(session:AsyncSession,name:str):
    genre = Genre(name=name)
    session.add(genre)
    await session.commit()
    return genre

async def add_book(session: AsyncSession, title: str, author_id: int, genre_id: int):
    book = Book(title=title, author_id=author_id, genre_id=genre_id)
    session.add(book)
    await session.commit()
    return book


async def get_books(session: AsyncSession):
    result = await session.execute(select(Book).options(joinedload(Book.author), joinedload(Book.genre)))
    return result.scalars().all()


async def get_book_by_id(session: AsyncSession, book_id: int):
    result = await session.execute(
        select(Book).where(Book.id == book_id).options(joinedload(Book.author), joinedload(Book.genre))
    )
    return result.scalar()


async def delete_book(session:AsyncSession,book_id:int):
    result = await session.execute(select(Book).where(Book.id))
    book = result.scalar()
    if book:
        await session.delete(book)
        await session.commit()
        return True
    return False