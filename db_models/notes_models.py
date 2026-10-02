from datetime import datetime
from sqlalchemy import ForeignKey, Text, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from connection_data.base import Base


class NotesORM(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id",
                                                    ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.utcnow
    )

    user: Mapped["UsersORM"] = relationship(
        # "UsersORM",
        back_populates="notes"
    )  # type: ignore
