from Directions import Directions
from Tile import Tile
import random


class Particle:
    def __init__(self, x, y, color):
        self.column = x
        self.row = y
        self.color = color

    def move(self, available_map):
        direction = random.choice(list(Directions))

        next_column, next_row = self.column + direction.value[0], self.row + direction.value[1]

        if available_map.position_is_available(next_column, next_row):
            self.column = next_column
            self.row = next_row

    def get_color(self):
        return self.color

    def __str__(self):
        return "Pos: [" + str(self.row) + ", " + str(self.column) + "]"
