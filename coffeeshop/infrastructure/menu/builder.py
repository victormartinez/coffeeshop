from decimal import Decimal
from typing import List, Tuple

from coffeeshop.infrastructure.menu.dto import Menu, MenuItem
from coffeeshop.domain.menu.interfaces import AbstractMenuBuilder


class SimpleMenuBuilder(AbstractMenuBuilder):

    def __init__(self, items: List[Tuple[str, Decimal, bool]]) -> None:
        self.items: MenuItem = [
            MenuItem(name=i[0], price=i[1], is_drink=i[2]) for i in items
        ]

    async def run(self) -> Menu:
        return Menu(items=self.items)
