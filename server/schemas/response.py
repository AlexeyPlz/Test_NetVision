from uuid import UUID

from pydantic import BaseModel


class MessageResponse(BaseModel):
    """Схема для вывода сообщений."""

    uuid: UUID
    text: str

    class Config:
        orm_mode = True
