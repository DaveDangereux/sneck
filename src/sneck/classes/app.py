import time

from sneck.classes.display import Display
from sneck.classes.game import Game
from sneck.classes.input import Input


class App:
    _FRAMES_PER_SECOND = 7

    def __init__(self):
        self._input = Input()
        self._display = Display()
        self._game = Game(self._display)

        self._frame_duration = 1.0 / self._FRAMES_PER_SECOND

    def run(self):
        while True:
            key = self._input.get_key()
            self._game.handle_input(key)
            output = self._game.get_output()
            self._game.run()
            self._display.display_output(output)
            time.sleep(self._frame_duration)
