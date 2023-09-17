from abc import ABC, abstractmethod

from .entity import Command


class LanguageParser(ABC):

    @abstractmethod
    async def run(self, sentence: str) -> Command:
        pass
