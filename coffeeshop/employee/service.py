from coffeeshop import nlp, cart
from coffeeshop.entities import Order, OrderAction


SUGGESTED_COOKIE = False


async def _should_upsell_cookie():
    if cart.is_empty():
        return False
    
    if SUGGESTED_COOKIE:
        return False
    
    if cart.has_cookie():
        return False
    
    return cart.is_previous_drink()


async def process(guest_sentence: str) -> str:
    order: Order = await nlp.parse_sentence(guest_sentence)
    if order.is_item():
        cart.update(order)
        if await _should_upsell_cookie():
            return "Would you like to add a cookie for $0.50?"
        return "Would you like anything else?"
    
    action: OrderAction = order
    if action.is_think():
        # TODO: Implement wait 10 seconds
        return "Please let me know when you are ready."
    
    if action.is_yes():
        # Guest wants the Cookie upsell
        cart.add_cookie()
        return "Would you like anything else?"
        
    if action.is_no():
        # Guest does not want the Cookie upsell
        return "Would you like anything else?"
    
    if action.is_finish():
        total = cart.calc_total()
        cart.flush()
        return f"Your total is ${total}. Thank you and have a nice day!"

    return "I don't understand."
    