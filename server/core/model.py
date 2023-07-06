import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:
    """Базовая модель."""

    __name__: str

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class Message(Base):
    """Модель сообщения."""

    __tablename__ = "messages"

    text = Column(String(16), nullable=False)

    def __repr__(self) -> str:
        return f"<Message - uuid: {self.uuid} - text: {self.text}>"
