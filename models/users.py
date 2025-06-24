from . import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class Users(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(200))
    cult_token: Mapped[str] = mapped_column(db.String(200))
    latitude: Mapped[str] = mapped_column(db.String(50))
    longitude: Mapped[str] = mapped_column(db.String(50))

    preferences: Mapped[List["Preferences"]] = relationship(
        "Preferences", back_populates="user", cascade="all, delete", lazy=True
    )

    def __repr__(self):
        return f"<User {self.id}: {self.name}>"
