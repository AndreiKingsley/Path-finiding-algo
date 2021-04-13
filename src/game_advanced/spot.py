from src.game_advanced.spot_state import *


class Spot:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.state = SpotState.EMPTY
        self.is_visible = False
        self.neighbors = []

    def get_color(self):
        return get_color(self.state, self.is_visible)

    def get_pos(self):
        return self.i, self.j

    # клетка - препятствие
    def is_barrier(self):
        return self.state == SpotState.BARRIER

    # стартовая клетка
    def is_start(self):
        return self.state == SpotState.START

    # целевая клетка
    def is_end(self):
        return self.state == SpotState.END

    # обычная клетка
    def reset(self):
        self.is_visible = False
        self.state = SpotState.EMPTY

    def make_start(self):
        self.state = SpotState.START

    def make_barrier(self):
        self.state = SpotState.BARRIER

    def make_end(self):
        self.state = SpotState.END

    def make_visible(self):
        self.is_visible = True

    def make_unvisible(self):
        self.is_visible = False

