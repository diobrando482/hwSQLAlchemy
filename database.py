from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine  
from sqlalchemy.orm import sessionmaker  

DATABASE_URL = 'mysql+aiomysql://user:password@localhost/dbname'  

engine = create_async_engine(DATABASE_URL, echo=True)  
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  

async def init_db():  
    from models import Base  
    async with engine.begin() as conn:  
        await conn.run_sync(Base.metadata.create_all)  
