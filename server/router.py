from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv

from server.core.service import MessageService
from server.schemas.request import СreateMessageRequest
from server.schemas.response import MessageResponse

router = APIRouter(prefix="/messages", tags=["Message"])


@cbv(router)
class MessageCBV:
    """CBV для работы с сообщениями."""

    __message_service: MessageService = Depends()

    @router.post(
        '/new',
        response_model=MessageResponse,
        status_code=HTTPStatus.CREATED,
        summary="Создать сообщение."
    )
    async def create(self, schema: СreateMessageRequest) -> MessageResponse:
        """
        Поля для создания сообщения.

        - **text**: текст сообщения
        """
        return await self.__message_service.create(schema)

    @router.get(
        '/all',
        response_model=list[MessageResponse],
        status_code=HTTPStatus.OK,
        summary="Получить список всех сообщений."
    )
    async def get_all(self) -> list[MessageResponse]:
        return await self.__message_service.get_all()

    @router.get(
        '/{count}',
        response_model=list[MessageResponse],
        status_code=HTTPStatus.OK,
        summary="Получить список нескольких сообщений."
    )
    async def get_count(self, count: int) -> list[MessageResponse]:
        return await self.__message_service.get_all(count)

    @router.get(
        '/{uuid}',
        response_model=MessageResponse,
        status_code=HTTPStatus.OK,
        summary="Получить сообщение."
    )
    async def get(self, uuid: UUID) -> MessageResponse:
        return await self.__message_service.get(uuid)

    @router.delete(
        '/{uuid}',
        response_model=None,
        status_code=HTTPStatus.OK,
        summary="Удалить сообщение."
    )
    async def delete(self, uuid: UUID) -> None:
        await self.__message_service.delete(uuid)
