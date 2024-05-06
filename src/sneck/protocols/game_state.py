from abc import abstractmethod
from typing import Protocol


class GameState(Protocol):
    @abstractmethod
    def run(self): ...
