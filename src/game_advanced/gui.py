import pygame

from src.game_advanced.colors import *
from src.game_advanced.grid import GridGame
from src.game_advanced.spot import Spot
from src.game_advanced.spot_state import *


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
        self.is_legend_open = False
        self.help_button_pos_and_rad = None
        self.legend_close_button_pos_and_rad = None

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
        self.is_legend_open = False
        self.help_button_pos_and_rad = ((self.width - 30, 30), 20)
        self.legend_close_button_pos_and_rad = ((self.width * 3 // 4, self.height // 4), 20)
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
        pygame.draw.rect(self.window, spot.get_color(), (x, y, self.cell_width, self.cell_height))

    def draw_current(self, i, j):
        x = j * self.cell_width
        y = i * self.cell_height
        pygame.draw.rect(self.window, get_color(SpotState.CURRENT, True), (x, y, self.cell_width, self.cell_height))

    def draw_path(self, i, j):
        x = j * self.cell_width
        y = i * self.cell_height
        pygame.draw.rect(self.window, get_color(SpotState.PATH, self.grid.grid[i][j].is_visible),
                         (x, y, self.cell_width, self.cell_height))

    def draw(self, current=None, path=None):
        self.window.fill(WHITE)
        
        for row in self.grid.grid:
            for spot in row:
                if (current is not None) or (path is not None):
                    if current is not None and current == (spot.i, spot.j):
                        self.draw_current(spot.i, spot.j)
                        continue
                    if path is not None and (spot.i, spot.j) in path:
                        self.draw_path(spot.i, spot.j)
                        continue
                    self.draw_spot(spot)
                else:
                    self.draw_spot(spot)
        self.draw_grid()
        
        # draw button
        smallfont = pygame.font.SysFont('Corbel',35)
        text = smallfont.render('?', True, (0, 0, 0))
        pygame.draw.circle(self.window, (255, 255, 255), self.help_button_pos_and_rad[0], 20, 0)
        self.window.blit(text, (self.width - 37, 20))
       
        if self.is_legend_open:
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
        self.grid.update(False)

    def update_grid_with_vision(self):
        self.grid.update(True)
        
    def is_help_button_pos(self, pos):
        w, h = self.help_button_pos_and_rad[0]
        r = self.help_button_pos_and_rad[1]
        return w - r <= pos[0] <= w + r and h - r <= pos[1] <= h + r
    
    def is_legend_close_button_pos(self, pos):
        w, h = self.legend_close_button_pos_and_rad[0]
        r = self.legend_close_button_pos_and_rad[1]
        return w - r <= pos[0] <= w + r and h - r <= pos[1] <= h + r
    
    def switch_legend(self):
        self.is_legend_open = not self.is_legend_open
        
    def draw_legend(self):
        HELP = ['SPACE - start the algorithm', 
                'r - clear the grid',
                'hold left click to draw barriers',
                'right click to remove barrier']
        pygame.draw.rect(self.window, (255, 255, 255), (self.width // 4, self.height // 4, self.width // 2, self.height // 4))
        smallfont = pygame.font.SysFont('Corbel', 35)
        text = smallfont.render('LEGEND', True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 4 + 30))
        self.window.blit(text, text_rect)
        for i, h in enumerate(HELP):
            smallfont = pygame.font.SysFont('Corbel', 35) 
            text = smallfont.render(h, True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.width // 2, self.height // 4 + 30 * (i + 2)))
            self.window.blit(text, text_rect)
            
        smallfont = pygame.font.SysFont('Corbel',35)
        text = smallfont.render('x', True, (0, 0, 0))
        pygame.draw.circle(self.window, (255, 255, 255), (self.width * 3 // 4, self.height // 4), 20, 0)
        text_rect = text.get_rect(center=self.legend_close_button_pos_and_rad[0])
        self.window.blit(text, text_rect)
        
        pygame.display.update()


# Singleton GUI
gui = GUI()
