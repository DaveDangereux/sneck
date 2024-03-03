from .board import Board
from .score_board_data import ScoreBoardData
from .screen import Screen
from .state_manager import StateManager


class Game:
    FPS = 7
    ROWS = 15
    COLS = 22

    def __init__(self):
        self.score = 0
        self.frame_duration = 1.0 / self.FPS
        self.score_board_data = ScoreBoardData()

        self.board = Board(self.ROWS, self.COLS)
        self.screen = Screen(self.ROWS, self.COLS)
        self.state_manager = StateManager(self)

    def run(self) -> None:
        while True:
            self.state_manager.run()
