from sneck.classes.text import Text
from sneck.enumerations import TextType

box_chars = {
    "top_left": Text("╔", TextType.WALL),
    "top_right": Text("╗", TextType.WALL),
    "bottom_left": Text("╚", TextType.WALL),
    "bottom_right": Text("╝", TextType.WALL),
    "horizontal_bar": Text("═", TextType.WALL),
    "vertical_bar": Text("║", TextType.WALL),
}

snake_chars = {"head": Text("█", TextType.SNAKE)}

fruit = Text("◉", TextType.FRUIT)
