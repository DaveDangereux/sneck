from abc import abstractmethod
from typing import Protocol


class GameState(Protocol):
    @abstractmethod
    def handle_input(self, key: str): ...

    @abstractmethod
    def run(self): ...
