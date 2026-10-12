from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass


# Database table
class AIModel(Base):
    __tablename__ = "ai_models"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    provider: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )