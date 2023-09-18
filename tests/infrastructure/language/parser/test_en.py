import pytest

from coffeeshop.infrastructure.language import factory
from coffeeshop.infrastructure.language.dto import (
    ActionType,
    ParsedActionDto,
    ParsedProductDto,
    ParsedSentenceDto,
)


@pytest.mark.parametrize(
    "sentence,expected",
    [
        (
            "I'd like a Latte.",
            ParsedSentenceDto(product=ParsedProductDto(add=True, name="LATTE")),
        ),
        (
            "I'd like a Macchiato.",
            ParsedSentenceDto(product=ParsedProductDto(add=True, name="MACCHIATO")),
        ),
        (
            "I'd like a Tea.",
            ParsedSentenceDto(product=ParsedProductDto(add=True, name="TEA")),
        ),
        (
            "I'd like a Cookie.",
            ParsedSentenceDto(product=ParsedProductDto(add=True, name="COOKIE")),
        ),
        (
            "I'd like an Americano.",
            ParsedSentenceDto(product=ParsedProductDto(add=True, name="AMERICANO")),
        ),
        (
            "I want something",
            ParsedSentenceDto(product=ParsedProductDto(add=True, name="SOMETHING")),
        ),
        (
            "I don't want a Latte.",
            ParsedSentenceDto(product=ParsedProductDto(add=False, name="LATTE")),
        ),
        (
            "I don't want a Macchiato.",
            ParsedSentenceDto(product=ParsedProductDto(add=False, name="MACCHIATO")),
        ),
        (
            "I don't want a Tea.",
            ParsedSentenceDto(product=ParsedProductDto(add=False, name="TEA")),
        ),
        (
            "I don't want a Cookie.",
            ParsedSentenceDto(product=ParsedProductDto(add=False, name="COOKIE")),
        ),
        (
            "I don't want an Americano.",
            ParsedSentenceDto(product=ParsedProductDto(add=False, name="AMERICANO")),
        ),
        (
            "That's all.",
            ParsedSentenceDto(action=ParsedActionDto(type=ActionType.FINISH)),
        ),
        (
            "Yes, please.",
            ParsedSentenceDto(action=ParsedActionDto(type=ActionType.YES)),
        ),
        (
            "No, thank you.",
            ParsedSentenceDto(action=ParsedActionDto(type=ActionType.NO)),
        ),
        ("", ParsedSentenceDto(action=ParsedActionDto(type=ActionType.UNKNOWN))),
    ],
)
@pytest.mark.asyncio
async def test_parse_sentence(sentence, expected):
    parser = await factory.create_parser()
    actual = await parser.run(sentence)
    assert actual == expected
