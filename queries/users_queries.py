import bcrypt
import logging

from sqlalchemy import select, text
from sqlalchemy.orm import joinedload, selectinload

from db_models import UsersORM, UserAccountsORM, NotesORM
from connection_data.connect import asyncsession
from pydantic_models.users import PydanticUser


def hash_password(pwd: str):
    bytes_password = pwd.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes_password, salt)


async def user_adding(kwargs: dict):
    async with asyncsession() as session:
        kwargs["password"] = hash_password(kwargs.get("password"))
        user = UsersORM(**kwargs)
        session.add(user)
        await session.flush()
        user_id = user.id
        await session.commit()
        return user_id


async def user_get(user_id: int):
    async with asyncsession() as session:
        query = select(
            UsersORM, user_id
            # type: ignore
        ).options(joinedload(UsersORM.notes), joinedload(UsersORM.account))
        result = await session.execute(query)
        # user = result.unique().scalar_one()

        # logging.info(f"Getting {user} - {type(user)}")

        res = PydanticUser.model_validate(
            result.unique().scalar_one_or_none(), from_attributes=True)
        return res


# async def user_updating(kwargs: dict):
#    async with asyncsession() as session
