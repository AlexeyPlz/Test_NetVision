import re

from pydantic import BaseModel, Extra, validator

VALID_TEXT = r"^[1-9A-Za-z]*$"
INVALID_SYM_TEXT_ERROR = "Для сообщения используются недопустимые символы."
INVALID_LEN_TEXT_ERROR = "Сообщение имеет количество символов отличное от 16."


class СreateMessageRequest(BaseModel):
    """Схема для создания сообщения."""

    text: str

    @validator('text')
    def validate_username(cls, value: str) -> str:
        if not (15 < len(value) < 17):
            raise ValueError(INVALID_LEN_TEXT_ERROR)
        if not re.compile(VALID_TEXT).match(value):
            raise ValueError(INVALID_SYM_TEXT_ERROR)
        return value

    class Config:
        extra = Extra.forbid
