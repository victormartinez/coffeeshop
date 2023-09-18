from decimal import Decimal
from typing import List, Tuple

from coffeeshop.domain.menu.interfaces import AbstractMenuBuilder, Menu
from coffeeshop.infrastructure.menu.dto import MenuDto, MenuItemDto


class SimpleMenuBuilder(AbstractMenuBuilder):
    def __init__(self, items: List[Tuple[str, Decimal, bool]]) -> None:
        self.items: List[MenuItemDto] = [
            MenuItemDto(name=i[0], price=i[1], is_drink=i[2]) for i in items
        ]

    async def run(self) -> Menu:
        return MenuDto(items=self.items)  # type: ignore[return-value]
