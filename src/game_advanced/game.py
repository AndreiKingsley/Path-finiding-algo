from src.game_advanced.gui import *
from src.game_advanced.open import OpenGame
from src.game_advanced.closed import ClosedGame
from src.game_advanced.vision import *

import pygame


# Функция для воостановления пути
def reconstruct_path(v):
    ans = []
    while v.parent is not None:
        ans.append((v.i, v.j))
        v = v.parent
    return ans[::-1]


def start_game(algorithm, your_open, your_closed, h, rows_number=40, cols_number=40, width=800, height=800, vision=3):
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
                    gui.draw(current=start_pos)
                    end_pos = (end.i, end.j)
                    cur = start_pos
                    while cur != end_pos:
                        make_visible(gui.get_grid(), cur, vision)
                        gui.update_grid_with_vision()
                        found_flag, last_v = algorithm(gui.get_grid(), cur, end_pos, OpenGame(your_open), ClosedGame(your_closed), h)
                        if not found_flag:
                            break
                        path = reconstruct_path(last_v)
                        spot = gui.get_spot(cur[0], cur[1])
                        if ((spot.i, spot.j) != start) and ((spot.i, spot.j) != end):
                            pass
                        gui.draw(current=cur, path=path)
                        cur = path[0]

                if event.key == pygame.K_r:
                    start = None
                    end = None
                    gui.reset(size, grid_size)
    gui.quit()
