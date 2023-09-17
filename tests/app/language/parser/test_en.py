import pytest

from coffeeshop.app.language import factory
from coffeeshop.app.language.entity import Command, Action



@pytest.mark.parametrize(
    "sentence,expected",
    [
        ("I'd like a Latte.", Command(add=True, product="LATTE", action=None)),
        ("I'd like a Macchiato.", Command(add=True, product="MACCHIATO", action=None)),
        ("I'd like a Tea.", Command(add=True, product="TEA", action=None)),
        ("I'd like a Cookie.", Command(add=True, product="COOKIE", action=None)),
        ("I'd like an Americano.", Command(add=True, product="AMERICANO", action=None)),
        ("I want something", Command(add=True, product="SOMETHING", action=None)),

        ("I don't want a Latte.", Command(add=False, product="LATTE", action=None)),
        ("I don't want a Macchiato.", Command(add=False, product="MACCHIATO", action=None)),
        ("I don't want a Tea.", Command(add=False, product="TEA", action=None)),
        ("I don't want a Cookie.", Command(add=False, product="COOKIE", action=None)),
        ("I don't want an Americano.", Command(add=False, product="AMERICANO", action=None)),

        ("That's all.", Command(action=Action.FINISH)),
        ("Yes, please.", Command(action=Action.YES)),
        ("No, thank you.", Command(action=Action.NO)),
        
        ("", Command(action=Action.UNKNOWN)),
    ],
)
@pytest.mark.asyncio
async def test_parse_sentence(sentence, expected):
    parser = factory.create_parser('en')
    actual = await parser.run(sentence)
    assert actual == expected
