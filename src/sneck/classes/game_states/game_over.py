from ...enumerations.text_type import TextType
from ...protocols.game_state import GameState
from ...protocols.state_manager_context import StateManagerContext
from ...tools import painter
from ..text import Text


class GameOverState(GameState):
    def __init__(self, state_manager: StateManagerContext):
        self.state_manager = state_manager
        self.game = state_manager.game

        self.game.screen.palette.load_default_theme()
        self.game.screen.disable_animation()

    def run(self):
        self.game.screen.erase()
        self.game.board.clear()
        painter.paint_centre_text(
            self.game.board,
            [
                Text("G A M E  O V E R", TextType.GAME_OVER),
                Text(""),
                Text(f"SCORE: {self.game.score:04d}", TextType.SCORE),
                Text(""),
                Text("Press space", TextType.INFO),
                Text("to continue", TextType.INFO),
            ],
        )

        self.game.screen.add_board(self.game.board)
        self.game.screen.refresh()

        while self.state_manager.state == self:
            self._process_user_input()

    def _process_user_input(self) -> None:
        try:
            key = self.game.screen.get_key()
        except Exception:
            key = ""

        if key == " ":
            self.state_manager.transition_to_score_board()
