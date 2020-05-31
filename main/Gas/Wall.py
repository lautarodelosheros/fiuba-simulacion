from WallType import WallType


class Wall:
    def __init__(self, type, size, reverse):
        self.type = type;
        self.size = size
        self.reversed = reverse

    def get_type(self):
        return self.type

    def get_size(self):
        return self.size

    def is_reversed(self):
        return self.reversed
