from sneck.classes.text import Text
from sneck.enumerations import TextType
from sneck.protocols.game_context import GameContext
from sneck.protocols.game_state import GameState


class GameOverState(GameState):
    def __init__(self, game: GameContext):
        self.game = game

        self.game.screen.palette.load_default_theme()
        self.game.screen.disable_animation()

    def run(self):
        self.game.screen.erase()
        self.game.board.clear()
        self.game.board.write_centre_text(
            [
                Text("G A M E  O V E R", TextType.GAME_OVER),
                Text(""),
                Text(f"SCORE: {self.game.score:04d}", TextType.SCORE),
                Text(""),
                Text("Press space", TextType.INFO),
                Text("to continue", TextType.INFO),
            ],
        )

        self.game.screen.draw_board(self.game.board)
        self.game.screen.refresh()

        while self.game.state == self:
            self._process_user_input()

    def _process_user_input(self) -> None:
        try:
            key = self.game.screen.get_key()
        except Exception:
            key = ""

        if key == " ":
            self.game.transition_to_score_board()
