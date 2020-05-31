from Directions import Directions
from Tile import Tile
import random

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move(self, available_map):
        direction = random.choice(list(Directions))

        next_x, next_y = self.x + direction.value[0], self.y + direction.value[1]

        if available_map.position_is_available(next_x, next_y):
            self.x = next_x
            self.y = next_y

    def get_color(self):
        return self.color

    def __str__(self):
        return "Pos: [" + str(self.row) + ", " + str(self.column) + "]"