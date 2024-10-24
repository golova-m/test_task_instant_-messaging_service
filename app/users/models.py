from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, int_pk, str_uniq
from datetime import date


# создаем модель таблицы студентов
class User(Base):
    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq]
    name: Mapped[str]
    email: Mapped[str_uniq]
    

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"name={self.name!r},"
                f"email={self.email!r})")

    def __repr__(self):
        return str(self)