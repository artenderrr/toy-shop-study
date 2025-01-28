from __future__ import annotations
from sqlalchemy import (
    Table,
    Column,
    String,
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from app.database import Base, engine


toy_tags_table = Table(
    "toy_tags",
    Base.metadata,
    Column("toy_name", ForeignKey("toys.name"), primary_key=True),
    Column("tag_name", ForeignKey("tags.name"), primary_key=True)
)

class ToyModel(Base):
    __tablename__ = "toys"

    name: Mapped[str] = mapped_column(String(64), primary_key=True)
    price: Mapped[int] = mapped_column(nullable=False)

    tags: Mapped[list[TagModel]] = relationship(
        secondary=toy_tags_table,
        back_populates="toys"
    )

class TagModel(Base):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(String(64), primary_key=True)

    toys: Mapped[list[ToyModel]] = relationship(
        secondary=toy_tags_table,
        back_populates="tags"
    )


Base.metadata.create_all(engine)