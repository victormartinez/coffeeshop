from coffeeshop.domain.cart.interfaces import AbstractCart
from coffeeshop.domain.menu.interfaces import Menu
from coffeeshop.domain.language.enums import ActionType
from coffeeshop.domain.language.interfaces import (
    AbstractLanguageParser,
    ParsedSentence,
    ParsedAction,
)


class OrderAiService:

    def __init__(self,
        lang_parser: AbstractLanguageParser,
        cart: AbstractCart,
        menu: Menu,
    ) -> None:
        self._lang_parser = lang_parser
        self._menu = menu
        self._cart = cart
        # TODO: upselling rules could be a class
        self._has_suggested_cookie = False

    async def reply(self, sentence: str) -> str:
        parsed_sentence: ParsedSentence = await self._lang_parser.run(sentence)
        if parsed_sentence.product:
            menu_item = await self._menu.get_item_by_name(parsed_sentence.product.name)
            if not menu_item:
                # TODO: better error handling
                raise Exception("Unknown")

            await self._cart.add(menu_item)
            if await self._should_upsell_cookie():
                return "Would you like to add a cookie for $0.50?"
            return "Would you like anything else?"

        if parsed_sentence.action:
            action: ParsedAction = parsed_sentence.action
            if action.type == ActionType.THINK:
                # TODO: Implement wait 10 seconds
                return "Please let me know when you are ready."
            
            if action.type == ActionType.YES:
                # Guest wants the Cookie upsell
                menu_item = await self._menu.get_item_by_name('COOKIE')
                if not menu_item:
                    # TODO: better error handling
                    raise Exception("Unknown")
                await self._cart.add(menu_item)
                return "Would you like anything else?"
                
            if action.type == ActionType.NO:
                # Guest does not want the Cookie upsell
                return "Would you like anything else?"
            
            if action.type == ActionType.FINISH:
                total = await self._cart.calc_total()
                return f"Your total is ${total}. Thank you and have a nice day!"

        raise Exception("Unknown")
    
    async def _should_upsell_cookie(self):
        if await self._cart.is_empty():
            return False
        
        if self._has_suggested_cookie:
            return False
        
        # TODO: fix Magic String
        if await self._cart.contains('COOKIE'):
            return False
        
        menu_item = await self._cart.get_previous()
        return menu_item.is_drink