from coffeeshop.app.service import OrderAiService
from coffeeshop.infrastructure.cart.factory import create_cart
from coffeeshop.infrastructure.language.factory import create_parser
from coffeeshop.infrastructure.menu.factory import create_menu


async def create_ai_service() -> OrderAiService:
    parser = await create_parser()
    cart = await create_cart()
    menu = await create_menu()
    return OrderAiService(lang_parser=parser, cart=cart, menu=menu)
