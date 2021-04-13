import pygame

from src.util import *
from src.grid import GridGame
from src.spot import Spot


class GUI:
    def __init__(self):
        self.size = None
        self.width = None
        self.height = None
        self.grid = None
        self.grid_size = None
        self.window = None
        self.cell_width = None
        self.cell_height = None
        self.rows = None
        self.columns = None

    def reset(self, size, grid_size):
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.grid_size = grid_size
        self.rows = grid_size[0]
        self.columns = grid_size[1]
        self.cell_width = self.width // self.rows
        self.cell_height = self.height // self.columns
        self.grid = GridGame(grid_size)
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.event.get()

    def start(self, size, grid_size):
        self.reset(size, grid_size)
        pygame.init()

    def draw_grid(self):
        for i in range(self.rows):
            pygame.draw.line(self.window, GREY, (0, i * self.cell_height), (self.width, i * self.cell_height))
        for j in range(self.columns):
            pygame.draw.line(self.window, GREY, (j * self.cell_width, 0), (j * self.cell_width, self.height))

    def draw_spot(self, spot: Spot):
        x = spot.j * self.cell_width
        y = spot.i * self.cell_height
        pygame.draw.rect(self.window, spot.color, (x, y, self.cell_width, self.cell_height))

    def draw(self):
        self.window.fill(WHITE)
        for row in self.grid.grid:
            for spot in row:
                self.draw_spot(spot)
        self.draw_grid()
        pygame.display.update()

    def quit(self):
        pygame.quit()
        # self.__init__()

    def get_clicked_pos(self, pos):
        x, y = pos
        row = y // self.cell_height
        col = x // self.cell_width
        return row, col

    def get_events(self):
        return pygame.event.get()

    def get_spot(self, i, j):
        return self.grid.grid[i][j]

    def get_grid(self):
        return self.grid

    def update_grid(self):
        self.grid.update()


# Singleton GUI
gui = GUI()
