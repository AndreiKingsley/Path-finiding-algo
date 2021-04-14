import pygame

from src.game_common.util import *
from src.game_common.grid import GridGame
from src.game_common.spot import Spot

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
        self.draw_legend()
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
        
    def _draw_info(self, HELP, title):
        pygame.draw.rect(self.window, (255, 255, 255), (self.width // 8, self.height // 4, self.width * 3 // 4, self.height // 4))
        smallfont = pygame.font.SysFont('Comic Sans MS', 35)
        text = smallfont.render(title, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 4 + 30))
        self.window.blit(text, text_rect)
        for i, h in enumerate(HELP):
            smallfont = pygame.font.SysFont('Comic Sans MS', 35) 
            text = smallfont.render(h, True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.width // 2, self.height // 4 + 32 * (i + 2)))
            self.window.blit(text, text_rect)
        
    def draw_legend(self):
        HELP = ['You see this banner, ',
                'it means that everything is cool.',
                '(We hope..)']
        self._draw_info(HELP, 'TEST')


# Singleton GUI
gui = GUI()


def start_game(rows_number=40, cols_number=40, width=800, height=800):
    run = True
    size = (width, height)
    grid_size = (rows_number, cols_number)
    gui.start(size=size, grid_size=grid_size)
    while run:
        gui.draw()
        for event in gui.get_events():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                run = False
    gui.quit()
