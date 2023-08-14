import pytest

from coffeeshop import nlp
from coffeeshop.entities import (
    OrderAction,
    OrderItem,
    OrderItemType,
    Action,
)


@pytest.mark.parametrize(
    "sentence,expected",
    [
        ("I'd like a Latte.", OrderItem(name="Latte", token="LATTE", type=OrderItemType.DRINK, price=2.13, add=True)),
        ("I'd like a Macchiato.", OrderItem(name="Macchiato", token="MACCHIATO", type=OrderItemType.DRINK, price=3.39, add=True)),
        ("I'd like a Tea.", OrderItem(name="Tea", token="TEA", type=OrderItemType.DRINK, price=1.75, add=True)),
        ("I'd like a Cookie.", OrderItem(name="Cookie", token="COOKIE", type=OrderItemType.BAKED, price=0.5, add=True)),
        ("I'd like an Americano.", OrderItem(name="Americano", token="AMERICANO", type=OrderItemType.DRINK, price=1.51, add=True)),

        ("I don't want a Latte.", OrderItem(name="Latte", token="LATTE", type=OrderItemType.DRINK, price=2.13, add=False)),
        ("I don't want a Macchiato.", OrderItem(name="Macchiato", token="MACCHIATO", type=OrderItemType.DRINK, price=3.39, add=False)),
        ("I don't want a Tea.", OrderItem(name="Tea", token="TEA", type=OrderItemType.DRINK, price=1.75, add=False)),
        ("I don't want a Cookie.", OrderItem(name="Cookie", token="COOKIE", type=OrderItemType.BAKED, price=0.5, add=False)),
        ("I don't want an Americano.", OrderItem(name="Americano", token="AMERICANO", type=OrderItemType.DRINK, price=1.51, add=False)),

        ("That's all.", OrderAction(type=Action.FINISH)),
        ("Yes, please.", OrderAction(type=Action.YES)),
        ("No, thank you.", OrderAction(type=Action.NO)),
        
        ("", OrderAction(type=Action.OTHER)),
        ("I want something", OrderAction(type=Action.OTHER)),
    ],
)
@pytest.mark.asyncio
async def test_parse_sentence(sentence, expected):
    actual = await nlp.parse_sentence(sentence)
    assert actual == expected
