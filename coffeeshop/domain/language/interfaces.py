from abc import ABC, abstractmethod
from typing import Optional, Protocol

from coffeeshop.domain.language.enums import ActionType
from coffeeshop.domain.language.dto import ParsedSentence


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
