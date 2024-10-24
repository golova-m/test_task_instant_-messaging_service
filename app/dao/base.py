from sqlalchemy.future import select
from app.database import async_session_maker


class BaseDAO:
    model = None


    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()