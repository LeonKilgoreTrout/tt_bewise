from datetime import datetime
from sqlalchemy import ForeignKey, inspect
from sqlalchemy.orm import (
    DeclarativeBase, relationship, Mapped, mapped_column
)


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]
    clues_count: Mapped[int]


class Question(Base):

    __tablename__ = 'questions'
    id: Mapped[int] = mapped_column(primary_key=True)
    answer: Mapped[str]
    question: Mapped[str]
    value: Mapped[int | None]
    airdate: Mapped[datetime]
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="cascade"))
    game_id: Mapped[int]
    invalid_count: Mapped[int | None]
    category: Mapped[Category] = relationship()
