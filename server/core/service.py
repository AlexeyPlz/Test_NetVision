from typing import Optional
from uuid import UUID

from fastapi import Depends

from server.core.model import Message
from server.core.repository import MessageRepository
from server.schemas.request import СreateMessageRequest


class MessageService:
    """Сервис для работы с сообщениями."""

    def __init__(self, message_repository: MessageRepository = Depends()) -> None:
        self.__message_repository = message_repository

    async def create(self, schema: СreateMessageRequest) -> Message:
        """Создать сообщение."""
        return await self.__message_repository.create(Message(**schema.dict()))

    async def get(self, uuid: UUID) -> Message:
        """Получить сообщение."""
        return await self.__message_repository.get(uuid)

    async def get_all(self, count: Optional[int] = None) -> list[Message]:
        """Получить список сообщений."""
        return await self.__message_repository.get_all(count)

    async def delete(self, uuid: UUID) -> None:
        """Удалить сообщение."""
        await self.__message_repository.delete(uuid)
