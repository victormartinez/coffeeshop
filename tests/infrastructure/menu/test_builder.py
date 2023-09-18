from decimal import Decimal

import pytest

from coffeeshop.infrastructure.menu.builder import SimpleMenuBuilder


@pytest.mark.asyncio
async def test_simple_builder():
    items = [
        ("AMERICANO", Decimal("1.51"), True),
        ("ESPRESSO", Decimal("1.27"), True),
        ("LATTE", Decimal("2.13"), True),
        ("MACCHIATO", Decimal("3.39"), True),
        ("TEA", Decimal("1.75"), True),
        ("COOKIE", Decimal("0.50"), False),
    ]
    builder = SimpleMenuBuilder(items)
    menu = await builder.run()
    assert len(menu.items) == 6
    assert menu.items[0].name == "AMERICANO"
    assert menu.items[0].price == Decimal("1.51")
    assert menu.items[0].is_drink is True
    assert menu.items[1].name == "ESPRESSO"
    assert menu.items[1].price == Decimal("1.27")
    assert menu.items[1].is_drink is True
    assert menu.items[2].name == "LATTE"
    assert menu.items[2].price == Decimal("2.13")
    assert menu.items[2].is_drink is True
    assert menu.items[3].name == "MACCHIATO"
    assert menu.items[3].price == Decimal("3.39")
    assert menu.items[3].is_drink is True
    assert menu.items[4].name == "TEA"
    assert menu.items[4].price == Decimal("1.75")
    assert menu.items[4].is_drink is True
    assert menu.items[5].name == "COOKIE"
    assert menu.items[5].price == Decimal("0.50")
    assert menu.items[5].is_drink is False
