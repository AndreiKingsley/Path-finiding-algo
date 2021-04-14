from src.game_common.gui import *
from src.game_common.open import OpenGame
from src.game_common.closed import ClosedGame

import pygame


# Функция для воостановления пути
def reconstruct_path(v):
    path = []
    while v.parent is not None:
        path += [v]
        v = v.parent
        spot = gui.get_spot(v.i, v.j)
        if not spot.is_end():
            spot.make_path()
        gui.draw()
    path += [v]
    spot = gui.get_spot(v.i, v.j)
    spot.make_start()
    gui.draw()
    return path


def start_game(algorithm, your_open, your_closed, h, rows_number=40, cols_number=40, width=800, height=800):
    run = True
    size = (width, height)
    grid_size = (rows_number, cols_number)
    gui.start(size=size, grid_size=grid_size)
    start = None
    end = None
    path_len = None
    nodes_created = None
    nodes_expanded = None
    while run:
        gui.draw()
        for event in gui.get_events():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                run = False
            if pygame.mouse.get_pressed()[0] and gui.is_help_button_pos(pygame.mouse.get_pos()):
                gui.switch_legend()
            elif pygame.mouse.get_pressed()[0] and gui.is_stats_button_pos(pygame.mouse.get_pos()):
                gui.switch_stats(path_len, nodes_created, nodes_expanded)
            elif pygame.mouse.get_pressed()[0]:  # LEFT CLICK
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
                    Open = OpenGame(your_open)
                    Closed = ClosedGame(your_closed)
                    found_flag, last_v = algorithm(gui.get_grid(), start_pos, end_pos, Open, Closed, h)
                    if found_flag:
                        path = reconstruct_path(last_v)
                        path_len = len(path)
                        nodes_created = len(Open) + len(Closed)
                        nodes_expanded = len(Closed)
                        
                if event.key == pygame.K_r:
                    start = None
                    end = None
                    gui.reset(size, grid_size)
    gui.quit()
