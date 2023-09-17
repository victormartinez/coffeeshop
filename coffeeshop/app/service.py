from coffeeshop.domain.cart.interfaces import AbstractCart
from coffeeshop.domain.menu.interfaces import Menu
from coffeeshop.domain.language.interfaces import AbstractLanguageParser


class OrderAiService:

    def __init__(self,
        lang_parser: AbstractLanguageParser,
        cart: AbstractCart,
        menu: Menu,
    ) -> None:
        self.lang_parser = lang_parser
        self.menu = menu
        self.cart = cart

    