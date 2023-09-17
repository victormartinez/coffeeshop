from abc import ABC, abstractmethod

from coffeeshop.domain.entity import Command


class LanguageParser(ABC):

    @abstractmethod
    async def run(self, sentence: str) -> Command:
        pass
