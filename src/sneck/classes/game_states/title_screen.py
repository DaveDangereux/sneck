from sneck.classes.text import Text
from sneck.enumerations import TextType
from sneck.protocols.game_context import GameContext
from sneck.protocols.game_state import GameState


class TitleScreenState(GameState):
    def __init__(self, game: GameContext):
        self.game = game
        self._board = game.output.board

        game.display.load_default_theme()
        self._board.clear()

        self._write_title_screen()

    def handle_input(self, key: str):
        if key == " ":
            self.game.transition_to_playing()

    def run(self): ...

    def _write_title_screen(self):
        self.game.output.board.write_centre_text(
            [
                Text("S N E C K", TextType.TITLE),
                Text("Press space", TextType.INFO),
                Text("to play", TextType.INFO),
            ],
        )
