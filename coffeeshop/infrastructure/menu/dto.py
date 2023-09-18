from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel


class MenuItemDto(BaseModel):
    name: str
    price: Decimal
    is_drink: bool


class MenuDto(BaseModel):
    items: List[MenuItemDto]

    async def get_item_by_name(self, name: str) -> Optional[MenuItemDto]:
        for item in self.items:
            if item.name.upper() == name.upper():
                return item
        return None
