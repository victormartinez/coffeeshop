from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List, Optional, Protocol


class MenuItem(Protocol):
    name: str
    price: Decimal
    is_drink: bool


class Menu(Protocol):
    items: List[MenuItem]

    async def get_item_by_name(self, name: str) -> Optional[MenuItem]:
        pass


class AbstractMenuBuilder(ABC):
    @abstractmethod
    async def run(self) -> Menu:
        pass
