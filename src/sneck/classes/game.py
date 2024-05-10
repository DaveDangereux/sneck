from sneck.classes.board import Board
from sneck.classes.display import Display
from sneck.classes.game_states import (GameOverState, PlayingState,
                                       ScoreBoardState, TitleScreenState)
from sneck.classes.output import Output
from sneck.classes.score_board_data import ScoreBoardData
from sneck.classes.text import Text
from sneck.enumerations.text_type import TextType
from sneck.protocols.game_context import GameContext


class Game(GameContext):
    def __init__(self, display: Display):
        self.display = display

        self.score_board_data = ScoreBoardData()

        board = Board(rows=15, cols=22)
        score_bar_text = Text("", TextType.SCORE_BAR)
        self.output = Output(board, score_bar_text)

        self.state = TitleScreenState(self)

        self.score = 0

    def handle_input(self, key: str):
        if key == "Q":
            self.display.stop()
            exit(0)

        self.state.handle_input(key)

    def run(self):
        self.state.run()

    def get_output(self):
        return self.output

    def transition_to_title_screen(self):
        self.state = TitleScreenState(self)

    def transition_to_playing(self):
        self.state = PlayingState(self)

    def transition_to_game_over(self):
        self.state = GameOverState(self)

    def transition_to_score_board(self):
        self.state = ScoreBoardState(self)
