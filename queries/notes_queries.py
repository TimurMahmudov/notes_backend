import logging

from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from db_models import UsersORM, NotesORM
from connection_data.connect import asyncsession

from pydantic_models import PydanticUser

logger = logging.basicConfig(
    level=logging.INFO,
    # filename='logs.log',
    # filemode='w',
    format='%(asctime)s %(levelname)s %(message)s'
)


async def notes_adding(kwargs: dict):
    async with asyncsession() as session:
        new_element = NotesORM(**kwargs)
        session.add(new_element)
        await session.commit()
        # await session.refresh(new_element)
        # user = await session.get(Users, kwargs.get("user_id"))
        query = select(
            UsersORM, kwargs.get("user_id")  # type: ignore
        ).options(selectinload(UsersORM.notes))
        res = await session.execute(query)
        user = res.scalar_one()
        logging.info(f"Getting {user} - {type(user)}")

        pyda_user = PydanticUser.model_validate(
            user, from_attributes=True)
        return pyda_user


async def updating(self, model_id: int, kwargs: dict):
    async with asyncsession() as session:
        await session.execute(
            update(self.model),
            [kwargs]
        )
        await session.commit()
