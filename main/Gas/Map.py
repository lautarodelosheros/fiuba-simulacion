from Tile import Tile


class Map:
    def __init__(self, dimensions):
        self.rows = dimensions["rows"] + 2
        self.columns = dimensions["columns"] + 3
        self.map = [[Tile.NONE for y in range(self.columns)] for x in
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

    def get_position(self, row, column):
        try:
            return self.map[row][column]
        except IndexError:
            print('error out of bounds', row, column, self.rows, self.columns)
            raise

    def get_rows_range(self):
        return range(1, self.rows)

    def get_half_columns_range(self, first_half=False):
        if first_half:
            return range(1, self.wall_column)
        return range(self.wall_column + 1, self.columns - 1)

    def get_columns_range(self):
        return range(1, self.columns - 1)

    def remove_wall(self, lower_half=False):
        if not lower_half:
            for x in range(1, self.rows // 2):
                self.map[x][self.wall_column] = Tile.NONE
        for x in range(self.rows // 2, self.rows - 1):
            self.map[x][self.wall_column] = Tile.NONE

    def __str__(self):
        return self.map.__str__()


if __name__ == '__main__':
    test = Map({"columns": 2, "rows": 2})

    print(test)

    print('----------------------------------')
    test.remove_wall()

    print(test)

    print('----------------------------------')

    test = Map({"columns": 2, "rows": 2})

    print(test)

    print('----------------------------------')
    test.remove_wall(True)

    print(test)
