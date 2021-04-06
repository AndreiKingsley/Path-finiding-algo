from gui import gui
from pygame import QUIT


class ClosedBase:
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def AddNode(self, item, *args):
        pass

    def WasExpanded(self, item, *args):
        pass


class ClosedGame(ClosedBase):
    def __init__(self, closed_class):
        self.closed = closed_class()

    def __iter__(self):
        return self.closed.__iter__()

    def __len__(self):
        return self.closed.__len__()

    def AddNode(self, item, *args):
        spot = gui.get_spot(item.i, item.j)
        if not spot.is_start() and not spot.is_end():
            spot.make_closed()
        gui.draw()
        for event in gui.get_events():
            if event == QUIT:
                gui.quit()
        return self.closed.AddNode(item, args)

    def WasExpanded(self, item, *args):
        return self.closed.WasExpanded(item, args)
