from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Protocol, List


class MenuItem(Protocol):
    name: str
    price: Decimal


class Menu(Protocol):
    items: List[MenuItem]


class AbstractMenuBuilder(ABC):

    @abstractmethod
    async def run(self) -> Menu:
        pass
