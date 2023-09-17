import pytest

from coffeeshop.app.language import factory
from coffeeshop.domain.entities.parsed_sentence import ParsedSentence, ParsedProduct, ParsedAction, ActionType



@pytest.mark.parametrize(
    "sentence,expected",
    [
        (
            "I'd like a Latte.",
            ParsedSentence(product=ParsedProduct(add=True, name="LATTE"))
        ),
        (
            "I'd like a Macchiato.",
            ParsedSentence(product=ParsedProduct(add=True, name="MACCHIATO"))
        ),
        (
            "I'd like a Tea.",
            ParsedSentence(product=ParsedProduct(add=True, name="TEA"))
        ),
        (
            "I'd like a Cookie.",
            ParsedSentence(product=ParsedProduct(add=True, name="COOKIE"))
        ),
        (
            "I'd like an Americano.",
            ParsedSentence(product=ParsedProduct(add=True, name="AMERICANO"))
        ),
        (
            "I want something",
            ParsedSentence(product=ParsedProduct(add=True, name="SOMETHING"))
        ),
        (
            "I don't want a Latte.",
            ParsedSentence(product=ParsedProduct(add=False, name="LATTE"))
        ),
        (
            "I don't want a Macchiato.",
            ParsedSentence(product=ParsedProduct(add=False, name="MACCHIATO"))
        ),
        (
            "I don't want a Tea.",
            ParsedSentence(product=ParsedProduct(add=False, name="TEA"))
        ),
        (
            "I don't want a Cookie.",
            ParsedSentence(product=ParsedProduct(add=False, name="COOKIE"))
        ),
        (
            "I don't want an Americano.",
            ParsedSentence(product=ParsedProduct(add=False, name="AMERICANO"))
        ),

        (
            "That's all.",
            ParsedSentence(action=ParsedAction(type=ActionType.FINISH))
        ),
        (
            "Yes, please.",
            ParsedSentence(action=ParsedAction(type=ActionType.YES))
        ),
        (
            "No, thank you.",
            ParsedSentence(action=ParsedAction(type=ActionType.NO))
        ),
        (
            "",
            ParsedSentence(action=ParsedAction(type=ActionType.UNKNOWN))
        ),
    ],
)
@pytest.mark.asyncio
async def test_parse_sentence(sentence, expected):
    parser = factory.create_parser('en')
    actual = await parser.run(sentence)
    assert actual == expected
