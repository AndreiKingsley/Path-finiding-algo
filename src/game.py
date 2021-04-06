from gui import *
from spot import Spot
from open import OpenGame
from closed import ClosedGame

import pygame


# Функция для воостановления пути
def reconstruct_path(v):
    while v.parent is not None:
        v = v.parent
        spot = gui.get_spot(v.i, v.j)
        if not spot.is_end():
            spot.make_path()
        gui.draw()
    spot = gui.get_spot(v.i, v.j)
    spot.make_start()
    gui.draw()


def start_game(algorithm, your_open, your_closed, h, rows_number=50, cols_number=50, width=1200, height=800):
    run = True
    size = (width, height)
    grid_size = (rows_number, cols_number)
    gui.start(size=size, grid_size=grid_size)
    start = None
    end = None
    while run:
        gui.draw()
        for event in gui.get_events():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                run = False
            if pygame.mouse.get_pressed()[0]:  # LEFT CLICK
                pos = pygame.mouse.get_pos()
                row, col = gui.get_clicked_pos(pos)
                spot = gui.get_spot(row, col)
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed()[2]:  # RIGHT CLICK
                pos = pygame.mouse.get_pos()
                row, col = gui.get_clicked_pos(pos)
                spot = gui.get_spot(row, col)
                spot.reset()
                if spot == start:
                    start = None
                if spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    gui.update_grid()
                    start_pos = (start.i, start.j)
                    end_pos = (end.i, end.j)
                    found_flag, last_v = algorithm(gui.get_grid(), start_pos, end_pos, OpenGame(your_open), ClosedGame(your_closed), h)
                    if found_flag:
                        reconstruct_path(last_v)
                if event.key == pygame.K_r:
                    start = None
                    end = None
                    gui.reset(size, grid_size)
    gui.quit()
