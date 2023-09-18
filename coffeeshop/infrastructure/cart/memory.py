from decimal import Decimal
from typing import List, Optional

from coffeeshop.domain.cart.interfaces import AbstractCart
from coffeeshop.domain.menu.interfaces import MenuItem


class InMemoryCart(AbstractCart):

    def __init__(self) -> None:
        self._cart: List[MenuItem] = []
    
    async def add(self, item: MenuItem) -> None:
        self._cart.append(item)

    async def get_items(self) -> List[MenuItem]:
        return self._cart

    async def is_empty(self) -> bool:
        return len(self._cart) == 0

    async def get_previous(self) -> Optional[MenuItem]:
        if self._cart:
            return self._cart[-1]
        return None
    
    async def contains(self, name: str) -> bool:
        try:
            next(filter(lambda i: i.name.upper() == name.upper(), self._cart))
            return True
        except StopIteration:
            return False

    async def calc_total(self) -> Decimal:
        return sum([i.price for i in self._cart])
