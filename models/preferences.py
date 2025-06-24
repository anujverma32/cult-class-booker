from typing import List
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.enums import Weekday, Class_timing, Class_type
from . import db


class Preferences(db.Model):
    __tablename__: str = "preferences"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey("users.id"))
    center: Mapped[int] = mapped_column()
    timing: Mapped[Class_timing] = mapped_column(SQLEnum(Class_timing))
    class_type: Mapped[Class_type] = mapped_column(SQLEnum(Class_type))
    _days_of_week: Mapped[str] = mapped_column("days_of_week", db.String(200))

    user: Mapped["Users"] = relationship("Users", back_populates="preferences")

    @property
    def days_of_week(self) -> List[Weekday]:
        if self._days_of_week:
            return [Weekday(int(s)) for s in self._days_of_week.split(",") if s]
        return []

    @days_of_week.setter
    def days_of_week(self, value: List[int]):
        self._days_of_week = ",".join(value)
        
    def __repr__(self):
        return f"<Preference {self.id}: User={self.user_id}, Center={self.center}, Timing={self.timing}, Type={self.class_type}, Days={self.days_of_week}>"

