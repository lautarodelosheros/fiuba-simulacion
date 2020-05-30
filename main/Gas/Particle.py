from Directions import Directions
from Tile import Tile
import random


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 1

    def move(self, available_map):
        direction = random.choice(list(Directions))

        x_direction = self.velocity * direction.value[0]
        y_direction = self.velocity * direction.value[1]
        new_x = self.x + x_direction
        new_y = self.y + y_direction

        if not available_map.get_position(new_x, new_y) == Tile.WALL:
            self.x = new_x
            self.y = new_y

    def __str__(self):
        return "Pos: [" + str(self.x) + ", " + str(self.y) + "]"
