from typing import Optional

from pydantic import BaseModel

from ...domain.language.enums import ActionType


class ParsedActionDto(BaseModel):
    type: ActionType


class ParsedProductDto(BaseModel):
    add: bool
    name: str


class ParsedSentenceDto(BaseModel):
    product: Optional[ParsedProductDto] = None
    action: Optional[ParsedActionDto] = None
