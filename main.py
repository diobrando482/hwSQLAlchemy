import asyncio
from db.database import async_session, init_db
from operations import add_author, add_genre, add_book, get_books, get_book_by_id, delete_book

async def main():
    await init_db()  # создаем таблицы

    async with async_session() as session:
        author = await add_author(session, "Толстой")
        genre = await add_genre(session, "Роман")
        book = await add_book(session, "Война и мир", author.id, genre.id)


        books = await get_books(session)
        for book in books:
            print(f"{book.id}: {book.title} (автор: {book.author.name}, жанр: {book.genre.name})")


        book = await get_book_by_id(session, 1)
        if book:
            print(f"Книга: {book.title} (автор: {book.author.name}, жанр: {book.genre.name})")

        success = await delete_book(session, 1)
        if success:
            print("Книга удалена.")
        else:
            print("Книга не найдена.")

if __name__ == "__main__":
    asyncio.run(main())
