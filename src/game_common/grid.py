from src.game_common.spot import Spot


class GridGame:
    def __init__(self, size):
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.grid = [[Spot(row, column) for column in range(self.width)] for row in range(self.height)]

    def update_spot(self, spot):
        row = spot.i
        col = spot.j
        if not spot.is_end() and not spot.is_start() and not spot.is_barrier():
            spot.reset()
        neighbors = []
        if row + 1 < self.height and not self.grid[row + 1][col].is_barrier():
            neighbors.append(self.grid[row + 1][col])
        if row > 0 and not self.grid[row - 1][col].is_barrier():
            neighbors.append(self.grid[row - 1][col])
        if col + 1 < self.width and not self.grid[row][col + 1].is_barrier():
            neighbors.append(self.grid[row][col + 1])
        if col > 0 and not self.grid[row][col - 1].is_barrier():
            neighbors.append(self.grid[row][col - 1])
        spot.neighbors = neighbors

    def update(self):
        for i in range(self.width):
            for j in range(self.height):
                self.update_spot(self.grid[i][j])

    def get_neighbors(self, i, j):
        return map(lambda spot: (spot.i, spot.j), self.grid[i][j].neighbors)

