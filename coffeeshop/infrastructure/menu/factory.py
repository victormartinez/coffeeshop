from decimal import Decimal

from coffeeshop.domain.menu.interfaces import Menu
from coffeeshop.infrastructure.menu.builder import SimpleMenuBuilder


async def create_menu() -> Menu:
    items = [
        ("AMERICANO", Decimal("1.51"), True),
        ("ESPRESSO", Decimal("1.27"), True),
        ("LATTE", Decimal("2.13"), True),
        ("MACCHIATO", Decimal("3.39"), True),
        ("TEA", Decimal("1.75"), True),
        ("COOKIE", Decimal("0.50"), False),
    ]
    builder = SimpleMenuBuilder(items)
    return await builder.run()
