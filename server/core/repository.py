from types import NoneType
from typing import Optional
from uuid import UUID

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from server.core.base import get_session
from server.core.exceptions import MessageNotFoundException
from server.core.model import Message


class MessageRepository:
    """Репозиторий для работы с сообщениями."""

    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        self._session = session

    async def create(self, instance: Message) -> Message:
        """Создать сообщение."""
        self._session.add(instance)
        await self._session.commit()
        await self._session.refresh(instance)
        return instance

    async def get(self, uuid: UUID) -> Message:
        """Получить сообщение."""
        message = await self._session.execute(select(Message).where(Message.uuid == uuid))
        message = message.scalars().first()
        if message is None:
            raise MessageNotFoundException()
        return message

    async def get_all(self, count: Optional[int] = None) -> list[Message]:
        """Получить список сообщений."""
        selects = {
            True: select(Message),
            False: select(Message).limit(count)
        }
        messages = await self._session.execute(selects[isinstance(count, NoneType)])
        return messages.scalars().all()

    async def delete(self, uuid: UUID) -> None:
        """Удалить сообщение."""
        message = await self.get(uuid)
        await self._session.delete(message)
        await self._session.commit()
