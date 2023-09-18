from abc import ABC, abstractmethod
from typing import Optional, Protocol

from coffeeshop.domain.language.enums import ActionType


class ParsedAction(Protocol):
    type: ActionType


class ParsedProduct(Protocol):
    add: bool
    name: str


class ParsedSentence(Protocol):
    product: Optional[ParsedProduct] = None
    action: Optional[ParsedAction] = None


class AbstractSentenceCleaner(ABC):

    @abstractmethod
    async def clean(self, sentence: str) -> str:
        pass


class AbstractLanguageParser(ABC):

    def __init__(self, cleaner: AbstractSentenceCleaner) -> None:
        self.cleaner = cleaner

    @abstractmethod
    async def run(self, sentence: str) -> ParsedSentence:
        pass
