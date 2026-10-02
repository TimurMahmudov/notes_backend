from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, text

from connection_data.base import Base  # type: ignore


class UsersORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.utcnow
    )

    account: Mapped["UserAccountsORM"] = relationship(back_populates="user")
    notes: Mapped[list["NotesORM"]] = relationship(
        # "NotesORM",
        back_populates="user",
    )

    def __repr__(self):
        return f"{self.username} - {self.updated_at}"


class UserAccountsORM(Base):
    __tablename__ = 'useraccounts'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id",
                                                    ondelete="CASCADE"))
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))

    user: Mapped["UsersORM"] = relationship(back_populates="account")
