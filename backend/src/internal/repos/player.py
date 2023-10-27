import logging
from typing import Any, Self
from uuid import UUID, uuid4

from fastapi import HTTPException
from sqlalchemy.orm.session import Session

from internal.models.player import PlayerDB


class PlayerRepo:
    def __init__(self: Self, db: Session) -> None:
        self.db: Session = db

    def find(self: Self) -> list[PlayerDB]:
        try:
            items: list[PlayerDB] = self.db.query(PlayerDB).all()
            return items

        except Exception as exc:
            logging.error(f"{repr(exc)=}")
            raise exc

    def find_by_id(self: Self, id_: UUID) -> PlayerDB:
        try:
            item: PlayerDB | None = self.db.query(PlayerDB).filter(PlayerDB.id == id_).scalar()
            if item is None:
                raise HTTPException(status_code=404, detail="Player with id: {id_} not found.")

            return item

        except Exception as exc:
            logging.error(f"{repr(exc)=}, {id=}")
            raise exc

    def create(self: Self, items: list[PlayerDB]) -> list[PlayerDB]:
        try:
            for item in items:
                if item.id is None:
                    item.id = uuid4()
                self.db.add(item)
                self.db.commit()
                self.db.refresh(item)

        except Exception as exc:
            logging.error(f"{repr(exc)=}")
            raise exc

        return items

    def update_by_id(self: Self, id_: UUID, item: dict[str, Any]) -> int:
        try:
            num_updated: int = self.db.query(PlayerDB).filter(PlayerDB.id == id_).update(item)
            self.db.commit()
            return num_updated

        except Exception as exc:
            logging.error(f"{repr(exc)=}")
            raise exc

    def delete_by_id(self: Self, id_: UUID) -> int:
        try:
            num_deleted: int = self.db.query(PlayerDB).filter(PlayerDB.id == id_).delete()
            self.db.commit()
            return num_deleted

        except Exception as exc:
            logging.error(f"{repr(exc)=}, {id_=}")
            raise exc
