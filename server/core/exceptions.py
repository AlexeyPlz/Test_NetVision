from http import HTTPStatus
from uuid import UUID

from fastapi.exceptions import HTTPException


class MessageNotFoundException(HTTPException):
    """Сообщение не найдено."""

    def __init__(self, uuid: UUID):
        super().__init__(status_code=HTTPStatus.NOT_FOUND, detail=f"Не найдено сообщение с uuid: {uuid}.", headers=None)
