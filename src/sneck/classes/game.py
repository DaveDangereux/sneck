from .board import Board
from .screen import Screen
from .state_manager import StateManager


class Game:
    FPS = 7
    ROWS = 15
    COLS = 22

    def __init__(self):
        self.score = 0
        self.frame_duration = 1.0 / self.FPS

        self.board = Board(self.ROWS, self.COLS)
        self.screen = Screen()
        self.state_manager = StateManager(self)

    def run(self) -> None:
        while True:
            self.state_manager.run()
