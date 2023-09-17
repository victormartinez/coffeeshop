from abc import ABC, abstractmethod

from coffeeshop.domain.entities.menu import Menu


class AbstractMenuBuilder(ABC):

    @abstractmethod
    async def run(self) -> Menu:
        pass
