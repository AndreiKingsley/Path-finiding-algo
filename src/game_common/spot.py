from src.game_common.util import *


class Spot:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.color = WHITE
        self.neighbors = []

    def get_pos(self):
        return self.i, self.j

    # клетка(вершина) лежит в CLOSED
    def is_closed(self):
        return self.color == RED

    # клетка(вершина) лежит в OPEN
    def is_open(self):
        return self.color == GREEN

    # клетка - препятствие
    def is_barrier(self):
        return self.color == BLACK

    # стартовая клетка
    def is_start(self):
        return self.color == ORANGE

    # целевая клетка
    def is_end(self):
        return self.color == TURQUOISE

    # обычная клетка
    def reset(self):
        self.color = WHITE

    # перекрасить клетку, если она попала в CLOSED
    def make_closed(self):
        self.color = RED

    def make_start(self):
        self.color = ORANGE

    # перекрасить клетку, если она попала в OPEN
    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    # клетка найденного пути
    def make_path(self):
        self.color = PURPLE

