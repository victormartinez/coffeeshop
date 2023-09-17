from decimal import Decimal
from typing import List

from pydantic import BaseModel


class MenuItem(BaseModel):
    name: str
    price: Decimal


class Menu(BaseModel):
    items: List[MenuItem]
