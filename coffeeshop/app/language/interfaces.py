from abc import ABC, abstractmethod

from coffeeshop.domain.entities.parsed_sentence import ParsedSentence


class AbstractLanguageParser(ABC):

    @abstractmethod
    async def run(self, sentence: str) -> ParsedSentence:
        pass
