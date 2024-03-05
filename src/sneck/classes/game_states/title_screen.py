from ...enumerations.text_type import TextType
from ...protocols.game_state import GameState
from ...protocols.state_manager_context import StateManagerContext
from ...tools import painter
from ..text import Text


class TitleScreenState(GameState):
    def __init__(self, state_manager: StateManagerContext):
        self.state_manager = state_manager
        self.game = state_manager.game

        self.game.screen.disable_animation()

    def run(self):
        self.game.screen.erase()
        self.game.board.clear()
        painter.paint_centre_text(
            self.game.board,
            [
                Text("S N A K E", TextType.TITLE),
                Text("Press space", TextType.INFO),
                Text("to play", TextType.INFO),
            ],
        )

        self.game.screen.add_board(self.game.board)
        self.game.screen.refresh()

        while self.state_manager.state == self:
            self._process_user_input()

    def _process_user_input(self):
        key = self.game.screen.get_key().upper()

        match key:
            case "Q":
                self.game.screen.stop()
                exit(0)
            case " ":
                self.state_manager.transition_to_playing()
