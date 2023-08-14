import re
from typing import Union

from .entities import Order, OrderItem, OrderAction, Action


async def parse_sentence(sentence: str) -> Order:
    cleaned_sentence = re.sub(r'[^\w\s]', '', sentence).upper()
    order_item = await _sentence_to_item(cleaned_sentence)
    if not order_item:
        return await _sentence_to_action(cleaned_sentence)
    return order_item


async def _sentence_to_item(cleaned_sentence: str) -> OrderItem:
    tokens = cleaned_sentence.split(" ")
    order_item_token = tokens[-1]
    should_add = 'DONT' not in tokens
    return OrderItem.build(token=order_item_token, add=should_add)


async def _sentence_to_action(cleaned_sentence: str) -> OrderAction:
    tokens = cleaned_sentence.split(" ")
    if "THATS" in tokens and "ALL" in tokens:
        return OrderAction(type=Action.FINISH)
    
    if "YES" in tokens and "PLEASE" in tokens:
        return OrderAction(type=Action.YES)
    
    if "NO" in tokens and "THANK" in tokens:
        return OrderAction(type=Action.NO)

    if "LET" in tokens and "THINK" in tokens:
        return OrderAction(type=Action.THINK)
    
    return OrderAction(type=Action.OTHER)
