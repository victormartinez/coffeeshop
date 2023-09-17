from enum import Enum, auto
from typing import Optional

from pydantic import BaseModel


class Action(Enum):
    FINISH = auto()
    YES = auto()
    NO = auto()
    THINK = auto()
    UNKNOWN = auto()


class Command(BaseModel):
    add: bool = False
    product: Optional[str] = None
    action: Optional[Action] = None

    def is_item(self):
        return bool(self.product)

    def is_action(self):
        return bool(self.action)

    def is_finish(self):
        return self.action == Action.FINISH

    def is_yes(self):
        return self.action == Action.YES

    def is_no(self):
        return self.action == Action.NO

    def is_think(self):
        return self.action == Action.THINK

    def is_unknown(self):
        return self.action == Action.UNKNOWN
