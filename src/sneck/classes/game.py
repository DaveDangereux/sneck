from sneck.classes.board import Board
from sneck.classes.game_states import (GameOverState, PlayingState,
                                       ScoreBoardState, TitleScreenState)
from sneck.classes.score_board_data import ScoreBoardData
from sneck.classes.screen import Screen
from sneck.protocols.game_context import GameContext


class Game(GameContext):
    FPS = 7
    ROWS = 15
    COLS = 22

    def __init__(self):
        self.score = 0
        self.frame_duration = 1.0 / self.FPS
        self.score_board_data = ScoreBoardData()

        self.board = Board(self.ROWS, self.COLS)
        self.screen = Screen(self.ROWS, self.COLS)

        self.state = TitleScreenState(self)

    def run(self) -> None:
        while True:
            self.state.run()

    def transition_to_title_screen(self):
        self.state = TitleScreenState(self)

    def transition_to_playing(self):
        self.state = PlayingState(self)

    def transition_to_game_over(self):
        self.state = GameOverState(self)

    def transition_to_score_board(self):
        self.state = ScoreBoardState(self)
