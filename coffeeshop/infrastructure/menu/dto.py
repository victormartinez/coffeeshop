from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel


class MenuItem(BaseModel):
    name: str
    price: Decimal
    is_drink: bool


class Menu(BaseModel):
    items: List[MenuItem]

    async def get_item_by_name(self, name: str) -> Optional[MenuItem]:
        for item in self.items:
            if item.name.upper() == name.upper():
                return item
        return None
