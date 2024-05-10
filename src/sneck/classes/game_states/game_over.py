from sneck.classes.text import Text
from sneck.enumerations import TextType
from sneck.protocols.game_context import GameContext
from sneck.protocols.game_state import GameState


class GameOverState(GameState):
    def __init__(self, game: GameContext):
        # game aliases
        self._game = game
        self._board = game.output.board
        self._score_bar_text = game.output.score_bar_text
        self._display = game.display

        self._board.clear()
        self._score_bar_text.clear()
        self._display.load_default_theme()

        self._write_game_over_screen()

    def handle_input(self, key: str) -> None:
        if key == " ":
            self._game.transition_to_score_board()

    def run(self): ...

    def _write_game_over_screen(self):
        self._board.write_centre_text(
            [
                Text("G A M E  O V E R", TextType.GAME_OVER),
                Text(""),
                Text(f"SCORE: {self._game.score:04d}", TextType.FINAL_SCORE),
                Text(""),
                Text("Press space", TextType.INFO),
                Text("to continue", TextType.INFO),
            ],
        )
