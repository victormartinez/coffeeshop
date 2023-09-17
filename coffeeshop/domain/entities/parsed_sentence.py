from enum import Enum, auto
from typing import Optional

from pydantic import BaseModel


class ActionType(Enum):
    FINISH = auto()
    YES = auto()
    NO = auto()
    THINK = auto()
    UNKNOWN = auto()


class ParsedAction(BaseModel):
    type: ActionType

    def is_finish(self):
        return self.type == ActionType.FINISH

    def is_yes(self):
        return self.type == ActionType.YES

    def is_no(self):
        return self.type == ActionType.NO

    def is_think(self):
        return self.type == ActionType.THINK

    def is_unknown(self):
        return self.type == ActionType.UNKNOWN


class ParsedProduct(BaseModel):
    add: bool
    name: str


class ParsedSentence(BaseModel):
    product: Optional[ParsedProduct] = None
    action: Optional[ParsedAction] = None

    def is_product(self):
        return bool(self.product)

    def is_action(self):
        return bool(self.action)
