# Sneck

A terminal-based recreation of the classic Nokia mobile game
[Snake](https://en.wikipedia.org/wiki/Snake_(1998_video_game)).

Made with Python 🐍.


## What is Snake?

Snake was a preloaded game on certain Nokia mobile phone models released in
1998. The objective of the game was to guide a moving snake around the screen and
consume randomly-appearing fruit, which caused the snake to grow in length.
Colliding with the snake's body or the sides of the screen resulted in a Game
Over ☠️.


## Why is Snake?

This was a small project inspired by a challenge set at [CodeHub
Bristol](https://www.meetup.com/codehub-bristol/)'s [Python
Dojo](https://bristol.github.io/code-hub-bristol/python-code-dojo-workshop-wednesdays-date/)
event. The Python Dojo is a fortnightly meetup where coders gather, split into
small teams and try to solve a challenge in under two hours. The event is very
informal and the emphasis is on learning, rather than necessarily completing the
task.

That evening, the challenge produced a lot of learning, but the result was far
from functional. However, the objective was compelling enough to take home and
turn into a personal learning project for a week or two.


## Screenshots

![Early Game](https://github.com/DaveDangereux/sneck/assets/61416292/1da49e32-d317-43b2-9092-3d2e4acc11e9)
![Blood Theme](https://github.com/DaveDangereux/sneck/assets/61416292/b0683abe-df21-46f8-9cec-e0931e55ef04)
![Pink Theme](https://github.com/DaveDangereux/sneck/assets/61416292/40de4aa8-fe33-4b10-a826-4473cc707e54)

*Screenshots showing a selection of colour schemes, unlocked every 100 points.*


## Installation

This project uses [Poetry](https://python-poetry.org/) to manage dependencies.

To run the project, use the following command:

```bash
make
```

If Make is not available on your system, you can also run:

```bash
poetry install
poetry run python -m sneck
```

Windows compatibility is not confirmed yet - see [Known
Issues](https://github.com/DaveDangereux/sneck/tree/dave/dt-58-update-readme?tab=readme-ov-file#known-issues).


## Controls

The game is played with [Vim](https://en.wikipedia.org/wiki/Vim_(text_editor))
navigation keys, so if you are a Vim user or would like the opportunity to
practice, this game will also serve as a handy training tool.

Basic movement keys are:

* `H` - Left
* `J` - Down
* `K` - Up
* `L` - Right

The game can be quit at any point by pressing `Q`.


## Planned Features

* Option to switch controls to regular cursor keys or WSAD
* Sound effects


## Known Issues

The `curses` module that this project depends on is part of the Python standard
library, but is not available on Windows. There are workarounds for this -
third-party projects exist to make `curses` available, but as I don't have
regular access to a Windows computer, this issue may remain on the backlog for a
while.


## Author
[David Jordan](https://github.com/davedangereux)
