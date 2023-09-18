from coffeeshop.domain.language.interfaces import AbstractLanguageParser
from coffeeshop.infrastructure.language.parser.en import EnParser


async def create_parser() -> AbstractLanguageParser:
    return EnParser()
