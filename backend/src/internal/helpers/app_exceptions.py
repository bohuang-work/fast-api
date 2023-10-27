from enum import Enum
from typing import Self

from fastapi import status


class AppExceptionType(Enum):
    # Application specific exceptions
    ERROR_ID_DOES_NOT_EXIST = "id does not exist"
    ERROR_INVALID_VALUE = "invalid value"


class AppException(Exception):  # noqa: N818
    def __init__(
        self: Self,
        type_: AppExceptionType,
        detail: str | None = None,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ) -> None:
        super().__init__()
        self.type: AppExceptionType = type_
        self.detail: str | None = detail
        self.status_code: int = status_code

    def __str__(self: Self) -> str:
        return f"type={self.type}, detail={self.detail}, status_code={self.status_code}"

    def __repr__(self: Self) -> str:
        return f"type={self.type}, detail={self.detail}, status_code={self.status_code}"
