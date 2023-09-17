import re
from typing import List

from coffeeshop.app.language.interfaces import LanguageParser
from coffeeshop.domain.entity import Command, Action


class EnParser(LanguageParser):

    async def run(self, sentence: str) -> Command:
        cleaned_sentence = re.sub(r'[^\w\s]', '', sentence).upper()
        tokens = cleaned_sentence.split(" ")
        intent_tokens = ["ID", "DONT", "LIKE", "WANT"]
        is_product = len(set(intent_tokens).intersection(tokens))
        if is_product:
            return await self._parse_product(tokens)
        return await self._parse_action(tokens)

    async def _parse_product(self, tokens: List[str]) -> Command:
        order_item_token = tokens[-1]
        should_add = 'DONT' not in tokens
        return Command(product=order_item_token, add=should_add)

    async def _parse_action(self, tokens: List[str]) -> Command:
        if "THATS" in tokens and "ALL" in tokens:
            return Command(action=Action.FINISH)
        
        if "YES" in tokens and "PLEASE" in tokens:
            return Command(action=Action.YES)
        
        if "NO" in tokens and "THANK" in tokens:
            return Command(action=Action.NO)

        if "LET" in tokens and "THINK" in tokens:
            return Command(action=Action.THINK)
        
        return Command(action=Action.UNKNOWN)