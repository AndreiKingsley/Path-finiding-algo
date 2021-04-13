class OpenBase:
    def __init__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def is_empty(self):
        pass

    def add_node(self, item):
        pass

    def get_best_node(self):
        pass


class OpenGame(OpenBase):
    def __init__(self, open_class):
        self.open = open_class()

    def __len__(self):
        return self.open.__len__()

    def __iter__(self):
        return self.open.__iter__()

    def is_empty(self):
        return self.open.is_empty()

    def add_node(self, item):
        return self.open.add_node(item)

    def get_best_node(self):
        return self.open.get_best_node()
