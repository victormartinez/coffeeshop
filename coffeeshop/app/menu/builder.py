from decimal import Decimal
from typing import Any, List, Tuple

from coffeeshop.domain.entities.menu import Menu, MenuItem

from .interfaces import AbstractMenuBuilder


class SimpleMenuBuilder(AbstractMenuBuilder):

    def __init__(self, items: List[Tuple[str, Decimal]]) -> None:
        self.items: MenuItem = [
            MenuItem(name=i[0], price=i[1]) for i in items
        ]

    def run(self) -> Menu:
        return Menu(items=self.items)
