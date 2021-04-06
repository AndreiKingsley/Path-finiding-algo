from gui import gui


class OpenBase:
    def __init__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def isEmpty(self):
        pass

    def AddNode(self, item):
        pass

    def GetBestNode(self):
        pass


class OpenGame(OpenBase):
    def __init__(self, open_class):
        self.open = open_class()

    def __len__(self):
        return self.open.__len__()

    def __iter__(self):
        return self.open.__iter__()

    def isEmpty(self):
        return self.open.isEmpty()

    def AddNode(self, item):
        spot = gui.get_spot(item.i, item.j)
        if not spot.is_start() and not spot.is_end():
            spot.make_open()
        gui.draw()
        return self.open.AddNode(item)

    def GetBestNode(self):
        return self.open.GetBestNode()
