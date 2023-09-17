from abc import ABC, abstractmethod

from coffeeshop.domain.menu.interfaces import MenuItem



class AbstractCart(ABC):

    def add(self, item: MenuItem) -> None:
        pass

    def get_items(self):
        pass

    def calc_total(self):
        pass
