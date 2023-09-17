from abc import ABC, abstractmethod
from typing import Optional, Protocol

from coffeeshop.app.language.enums import ActionType
from coffeeshop.app.language.dto import ParsedSentence


class ParsedAction(Protocol):
    type: ActionType


class ParsedProduct(Protocol):
    add: bool
    name: str


class ParsedSentence(Protocol):
    product: Optional[ParsedProduct] = None
    action: Optional[ParsedAction] = None



class AbstractLanguageParser(ABC):
    @abstractmethod
    async def run(self, sentence: str) -> ParsedSentence:
        pass
