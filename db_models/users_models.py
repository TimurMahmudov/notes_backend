from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String

from connection_data.base import Base  # type: ignore


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    account: Mapped["UserAccounts"] = relationship(back_populates="user")
    notes: Mapped[list["Notes"]] = relationship(
        back_populates="user")  # type: ignore


class UserAccounts(Base):
    __tablename__ = 'useraccounts'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id",
                                                    ondelete="CASCADE"))
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))

    user: Mapped["Users"] = relationship(back_populates="account")
