from Directions import Directions
from Tile import Tile
import random


class Particle:
    def __init__(self, x, y, first_half=True):
        self.row = x
        self.column = y
        self.velocity = 1
        self.color = 'g' if first_half else 'r'

    def move(self, available_map):
        direction = random.choice(list(Directions))

        row_velocity = self.velocity * direction.value[0]
        column_velocity = self.velocity * direction.value[1]
        new_row = self.row + row_velocity
        new_column = self.column + column_velocity

        try:
            if not available_map.get_position(new_row, new_column) == Tile.WALL:
                self.row = new_row
                self.column = new_column
        except IndexError:
            self.row -= row_velocity
            self.column -= column_velocity

    def get_color(self):
        return self.color

    def __str__(self):
        return "Pos: [" + str(self.row) + ", " + str(self.column) + "]"
