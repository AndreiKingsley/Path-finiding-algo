import time

import pygame

from src.game_advanced.gui import gui


class ClosedBase:
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def add_node(self, item):
        pass

    def was_expanded(self, item):
        pass


class ClosedGame(ClosedBase):
    def __init__(self, closed_class):
        self.closed = closed_class()

    def __iter__(self):
        return self.closed.__iter__()

    def __len__(self):
        return self.closed.__len__()

    def add_node(self, item):
        return self.closed.add_node(item)

    def was_expanded(self, item):
        return self.closed.was_expanded(item)
