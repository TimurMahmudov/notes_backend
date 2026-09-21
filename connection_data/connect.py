from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from connection_data.config import settings


async_engine = create_async_engine(
    url=settings.async_db_connection_url,
    echo=True
)

asyncsession = async_sessionmaker(async_engine)
