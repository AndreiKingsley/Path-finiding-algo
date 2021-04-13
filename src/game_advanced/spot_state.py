from enum import Enum
from src.game_advanced.colors import *


class SpotState(Enum):
    EMPTY = 0
    BARRIER = 1
    START = 2
    END = 3
    PATH = 4
    CURRENT = 5


state_colors_visible = {
    SpotState.EMPTY: WHITE,
    SpotState.BARRIER: BLACK,
    SpotState.START: ORANGE,
    SpotState.END: BLUE,
    SpotState.PATH: PURPLE,
    SpotState.CURRENT: RED,
}

state_colors_not_visible = {
    SpotState.EMPTY: LIGHT_LIGHT_GREY,
    SpotState.BARRIER: DARK_GREY,
    SpotState.START: ORANGE,
    SpotState.END: LIGHT_BLUE,
    SpotState.PATH: LIGHT_PURPLE,
}


def get_color(state, is_visible):
    return state_colors_visible[state] if is_visible else state_colors_not_visible[state]
