from Tile import Tile

class Map:
    def __init__(self, columns, rows):
        self.columns = columns + 3
        self.rows = rows + 2
        self.map = [[Tile.NONE for x in range(self.columns)] for y in
                    range(self.rows)]

        for x in range(self.columns):
            self.map[0][x] = Tile.WALL
        for x in range(self.rows):
            self.map[x][0] = Tile.WALL
        for x in range(self.columns):
            self.map[- 1][x] = Tile.WALL
        for x in range(self.rows):
            self.map[x][-1] = Tile.WALL

        self.wall_column = self.columns // 2

        for x in range(self.rows):
            self.map[x][self.wall_column] = Tile.WALL

    def position_is_available(self, column, row):
        return self.map[row][column] != Tile.WALL

    def remove_wall(self, lower_half=False):
        if not lower_half:
            for x in range(1, self.rows // 2):
                self.map[x][self.wall_column] = Tile.NONE
        for x in range(self.rows // 2, self.rows - 1):
            self.map[x][self.wall_column] = Tile.NONE

    def __str__(self):
        return self.map.__str__()


if __name__ == '__main__':
    test = Map(2, 2)

    print(test)

    print('----------------------------------')
    test.remove_wall()

    print(test)

    print('----------------------------------')

    test = Map(2, 2)

    print(test)

    print('----------------------------------')
    test.remove_wall(True)

    print(test)