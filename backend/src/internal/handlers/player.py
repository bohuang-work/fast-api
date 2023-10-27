from uuid import UUID

from fastapi import status
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session

from internal.models.player import (
    PlayerCreateRequest,
    PlayerCreateResponse,
    PlayerDeleteResponse,
    PlayerFindResponse,
    PlayerUpdateRequest,
    PlayerUpdateResponse,
)
from internal.repos.player import PlayerRepo
from internal.repos.postgresql import get_session
from internal.services.player import PlayerService

router: APIRouter = APIRouter()


@router.get(
    "/v1/players/",
    summary="Find players.",
    response_model=list[PlayerFindResponse],
    status_code=status.HTTP_200_OK,
)
def find(
    session: Session = Depends(get_session),
) -> list[PlayerFindResponse] | None:
    """Find players."""
    repo: PlayerRepo = PlayerRepo(session)
    service: PlayerService = PlayerService(repo)
    return service.find()


@router.get(
    "/v1/player/{player_id}",
    summary="Find player by id.",
    response_model=PlayerFindResponse,
    status_code=status.HTTP_200_OK,
)
def find_by_id(
    player_id: UUID,
    session: Session = Depends(get_session),
) -> PlayerFindResponse | None:
    """Find player by id."""
    repo: PlayerRepo = PlayerRepo(session)
    service: PlayerService = PlayerService(repo)
    return service.find_by_id(id=player_id)


@router.post(
    "/v1/players/",
    summary="Create players.",
    response_model=list[PlayerCreateResponse],
    status_code=status.HTTP_201_CREATED,
)
def create(
    body: list[PlayerCreateRequest],
    session: Session = Depends(get_session),
) -> list[PlayerCreateResponse]:
    """create players."""
    repo: PlayerRepo = PlayerRepo(session)
    service: PlayerService = PlayerService(repo)
    return service.create(body=body)


@router.patch(
    "/v1/players/",
    summary="Update player by id.",
    response_model=PlayerUpdateResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def update(
    player_id: UUID,
    body: PlayerUpdateRequest,
    session: Session = Depends(get_session),
) -> PlayerUpdateResponse:
    """update players."""
    repo: PlayerRepo = PlayerRepo(session)
    service: PlayerService = PlayerService(repo)
    return service.update_by_id(id=player_id, body=body)


@router.delete(
    "/v1/player/{player_id}",
    summary="Delete player by id.",
    response_model=PlayerDeleteResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def delete_by_id(
    player_id: UUID,
    session: Session = Depends(get_session),
) -> PlayerDeleteResponse | None:
    """Delete player by id."""
    repo: PlayerRepo = PlayerRepo(session)
    service: PlayerService = PlayerService(repo)
    return service.delete_by_id(id=player_id)
