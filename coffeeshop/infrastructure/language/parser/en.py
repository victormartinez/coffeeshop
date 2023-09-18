from typing import List

from coffeeshop.domain.language.interfaces import AbstractLanguageParser
from coffeeshop.infrastructure.language.dto import (
    ParsedSentence,
    ParsedProduct,
    ParsedAction,
    ActionType,
)


class EnParser(AbstractLanguageParser):

    async def run(self, sentence: str) -> ParsedSentence:
        cleaned_sentence = await self.cleaner.clean(sentence)
        tokens = cleaned_sentence.split(" ")
        intent_tokens = ["ID", "DONT", "LIKE", "WANT"]
        is_product = len(set(intent_tokens).intersection(tokens))
        if is_product:
            product = await self._parse_product(tokens)
            return ParsedSentence(cleaned_sentence=cleaned_sentence, product=product)
        
        action = await self._parse_action(tokens)
        return ParsedSentence(cleaned_sentence=cleaned_sentence, action=action)

    async def _parse_product(self, tokens: List[str]) -> ParsedProduct:
        order_item_token = tokens[-1]
        should_add = 'DONT' not in tokens
        return ParsedProduct(add=should_add, name=order_item_token)

    async def _parse_action(self, tokens: List[str]) -> ParsedAction:
        if "THATS" in tokens and "ALL" in tokens:
            return ParsedAction(type=ActionType.FINISH)
        
        if "YES" in tokens and "PLEASE" in tokens:
            return ParsedAction(type=ActionType.YES)
        
        if "NO" in tokens and "THANK" in tokens:
            return ParsedAction(type=ActionType.NO)

        if "LET" in tokens and "THINK" in tokens:
            return ParsedAction(type=ActionType.THINK)
        
        return ParsedAction(type=ActionType.UNKNOWN)