from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List, Optional

from coffeeshop.domain.menu.interfaces import MenuItem


class AbstractCart(ABC):

    @abstractmethod
    async def add(self, item: MenuItem) -> None:
        pass

    @abstractmethod
    async def get_items(self) -> List[MenuItem]:
        pass

    @abstractmethod
    async def is_empty(self) -> bool:
        pass

    @abstractmethod
    async def get_previous(self) -> Optional[MenuItem]:
        pass

    @abstractmethod
    async def contains(self, name: str) -> bool:
        pass

    @abstractmethod
    async def calc_total(self) -> Decimal:
        pass
