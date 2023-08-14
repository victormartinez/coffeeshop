from typing import Optional

from enum import Enum, auto

from pydantic import BaseModel


class Action(Enum):
    FINISH = auto()
    YES = auto()
    NO = auto()
    THINK = auto()
    OTHER = auto()


class OrderItemType(Enum):
    DRINK = auto()
    BAKED = auto()


_MENU = {
    "AMERICANO": ("Americano", OrderItemType.DRINK, 1.51),
    "ESPRESSO": ("Espresso", OrderItemType.DRINK, 1.27),
    "LATTE": ("Latte", OrderItemType.DRINK, 2.13),
    "MACCHIATO": ("Macchiato", OrderItemType.DRINK, 3.39),
    "TEA": ("Tea", OrderItemType.DRINK, 1.75),
    "COOKIE": ("Cookie", OrderItemType.BAKED, 0.50),
}

class Order(BaseModel):

    def is_item(self):
        return hasattr(self, 'price')
    

class OrderItem(Order):
    name: str
    token: str
    type: OrderItemType
    price: float
    add: bool

    @classmethod
    def build(Cls, token: str, add: bool = True) -> Optional['OrderItem']:
        try:
            name, type_, price = _MENU[token]
            return Cls(name=name, token=token, type=type_, price=price, add=add)
        except KeyError:
            return None

    def is_drink(self):
        return self.type == OrderItemType.DRINK
    
    def is_cookie(self):
        return self.token == OrderItemType.DRINK


class OrderAction(Order):
    type: Action

    def is_finish(self):
        return self.type == Action.FINISH

    def is_yes(self):
        return self.type == Action.YES

    def is_no(self):
        return self.type == Action.NO

    def is_think(self):
        return self.type == Action.THINK

    def is_other(self):
        return self.type == Action.OTHER

