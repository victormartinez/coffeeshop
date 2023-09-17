from decimal import Decimal

from coffeeshop.app.menu.builder import SimpleMenuBuilder


def test_simple_builder():
    items = [
        ("AMERICANO", Decimal("1.51")),
        ("ESPRESSO", Decimal("1.27")),
        ("LATTE", Decimal("2.13")),
        ("MACCHIATO", Decimal("3.39")),
        ("TEA", Decimal("1.75")),
        ("COOKIE", Decimal("0.50")),
    ]
    menu = SimpleMenuBuilder(items).run()
    assert len(menu.items) == 6

    assert menu.items[0].name == "AMERICANO"
    assert menu.items[0].price == Decimal("1.51")
    assert menu.items[1].name == "ESPRESSO"
    assert menu.items[1].price == Decimal("1.27")
    assert menu.items[2].name == "LATTE"
    assert menu.items[2].price == Decimal("2.13")
    assert menu.items[3].name == "MACCHIATO"
    assert menu.items[3].price == Decimal("3.39")
    assert menu.items[4].name == "TEA"
    assert menu.items[4].price == Decimal("1.75")
    assert menu.items[5].name == "COOKIE"
    assert menu.items[5].price == Decimal("0.50")
    