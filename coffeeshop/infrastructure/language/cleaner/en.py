import re

from coffeeshop.domain.language.interfaces import AbstractSentenceCleaner


class EnSentenceCleaner(AbstractSentenceCleaner):
    async def clean(self, sentence: str) -> str:
        return re.sub(r"[^\w\s]", "", sentence.strip("\n")).upper()
