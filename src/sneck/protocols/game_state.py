from typing import Protocol


class GameState(Protocol):
    def run(self): ...
