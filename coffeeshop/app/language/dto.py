from enum import Enum, auto
from typing import Optional

from pydantic import BaseModel

from .enums import ActionType


class ParsedAction(BaseModel):
    type: ActionType


class ParsedProduct(BaseModel):
    add: bool
    name: str


class ParsedSentence(BaseModel):
    product: Optional[ParsedProduct] = None
    action: Optional[ParsedAction] = None
