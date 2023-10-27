from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.orm import (DeclarativeBase, Mapped, MappedAsDataclass,
                            mapped_column)


# Database model
class Base(DeclarativeBase, MappedAsDataclass):
    pass


class PlayerDB(Base):
    __tablename__ = "players"
    id: Mapped[UUID] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(nullable=False)
    height: Mapped[int] = mapped_column(nullable=False)
    team: Mapped[str] = mapped_column(nullable=False)
    active: Mapped[bool] = mapped_column(nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}  # type: ignore


# API model
class PlayerCreateRequest(BaseModel):
    name: str
    height: int
    team: str
    active: bool


class PlayerCreateResponse(BaseModel):
    id: UUID
    name: str


class PlayerFindResponse(BaseModel):
    id: UUID
    name: str
    height: int
    team: str
    active: bool


class PlayerUpdateRequest(BaseModel):
    name: str
    height: int
    team: str
    active: bool


class PlayerUpdateResponse(BaseModel):
    num_updated: int


class PlayerDeleteResponse(BaseModel):
    num_deleted: int
