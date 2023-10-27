from uuid import UUID

from internal.models.player import (
    PlayerCreateRequest,
    PlayerCreateResponse,
    PlayerDeleteResponse,
    PlayerFindResponse,
    PlayerUpdateRequest,
    PlayerUpdateResponse,
)
from internal.repos.player import PlayerDB, PlayerRepo


class PlayerService:
    def __init__(self, repo: PlayerRepo):
        self.repo = repo

    def find(self):
        player_db: list[PlayerDB] = self.repo.find()
        players: list[PlayerFindResponse] = []
        for player in player_db:
            players.append(PlayerFindResponse.model_validate(player.as_dict()))
        return players

    def find_by_id(self, id: UUID):
        player_db: PlayerDB = self.repo.find_by_id(id_=id)
        playter = PlayerFindResponse.model_validate(player_db.as_dict())
        return playter

    def create(self, body: list[PlayerCreateRequest]) -> list[PlayerCreateResponse]:
        items: list[PlayerDB] = []
        for item_body in body:
            items.append(
                PlayerDB(
                    name=item_body.name,
                    height=item_body.height,
                    team=item_body.team,
                    active=item_body.active,
                )
            )
        player_db: list[PlayerDB] = self.repo.create(items)
        players: list[PlayerCreateResponse] = []
        for player in player_db:
            players.append(PlayerCreateResponse(id=player.id, name=player.name))
        return players

    def update_by_id(self, id: UUID, body: PlayerUpdateRequest) -> PlayerUpdateResponse:
        num_updated: int = self.repo.update_by_id(id, dict(body))
        return PlayerUpdateResponse(num_updated=num_updated)

    def delete_by_id(self, id: UUID) -> PlayerDeleteResponse:
        num_deleted: int = self.repo.delete_by_id(id_=id)
        return PlayerDeleteResponse(num_deleted=num_deleted)
