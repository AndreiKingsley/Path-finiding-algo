from src.game_common.gui import gui
from pygame import QUIT


class ClosedBase:
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def add_node(self, item, *args):
        pass

    def was_expanded(self, item, *args):
        pass


class ClosedGame(ClosedBase):
    def __init__(self, closed_class):
        self.closed = closed_class()

    def __iter__(self):
        return self.closed.__iter__()

    def __len__(self):
        return self.closed.__len__()

    def add_node(self, item, *args):
        spot = gui.get_spot(item.i, item.j)
        if not spot.is_start() and not spot.is_end():
            spot.make_closed()
        gui.draw()
        for event in gui.get_events():
            if event == QUIT:
                gui.quit()
        return self.closed.add_node(item, args)

    def was_expanded(self, item, *args):
        return self.closed.was_expanded(item, args)
