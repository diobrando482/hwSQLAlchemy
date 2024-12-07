import asyncio  
from database import async_session, init_db  
from crud import add_author, add_genre, add_book, get_books, get_book_by_id, delete_book  

async def main():  
    await init_db()  

    async with async_session() as session:  
        author = await add_author(session, 'Author Name')  
        genre = await add_genre(session, 'Genre Name')  
        book = await add_book(session, 'Book Title', author.id, genre.id)  
 
        books = await get_books(session)  
        print('All books:', books)  

        book_details = await get_book_by_id(session, book.id)  
        print('Book details:', book_details)  

        await delete_book(session, book.id)  
        print(f'Book with ID {book.id} deleted.')  

asyncio.run(main())  
