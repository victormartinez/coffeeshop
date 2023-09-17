from enum import Enum, auto


class ActionType(Enum):
    FINISH = auto()
    YES = auto()
    NO = auto()
    THINK = auto()
    UNKNOWN = auto()
