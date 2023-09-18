from coffeeshop.domain.cart.interfaces import AbstractCart
from coffeeshop.infrastructure.cart.memory import InMemoryCart


async def create_cart() -> AbstractCart:
    return InMemoryCart()
