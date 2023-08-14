from typing import List
from coffeeshop.entities import Order, OrderItem, OrderAction


# TODO: flush it
_CART: List[OrderItem] = []


def is_empty() -> bool:
    return len(_CART) == 0


def update(item: OrderItem) -> None:
    if item.add:
        _CART.append(item)
    else:
        _CART.remove(item)


def add_cookie() -> None:
    item = OrderItem.build("COOKIE")
    update(item)


def has_cookie() -> bool:
    if not len(_CART):
        return False 
    return bool([item for item in _CART if item.is_cookie()])


def is_previous_drink() -> bool:
    if not len(_CART):
        return False 
    return _CART[-1].is_drink()


def calc_total():
    return sum([item.price for item in _CART])


def flush():
    _CART.clear()
