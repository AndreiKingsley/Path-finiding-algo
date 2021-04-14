import time

from src.game_advanced.gui import *
from src.game_advanced.open import OpenGame
from src.game_advanced.closed import ClosedGame
from src.game_advanced.vision import *
import pygame_menu
from pygame_menu.examples import create_example_window
import time
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
    found_path = None
    path_len = None
    while run:
        if found_path is not None:
            gui.draw(current=start_pos, path=found_path)
        else:
            gui.draw()
        for event in gui.get_events():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                run = False
            if pygame.mouse.get_pressed()[0] and gui.is_help_button_pos(pygame.mouse.get_pos()):
                gui.switch_legend()
            elif pygame.mouse.get_pressed()[0] and gui.is_stats_button_pos(pygame.mouse.get_pos()):
                gui.switch_stats(path_len)
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
                    found_path = None
                    gui.update_grid()
                    start_pos = (start.i, start.j)
                    gui.draw(current=start_pos)
                    end_pos = (end.i, end.j)
                    cur = start_pos
                    res_path = [cur]
                    while cur != end_pos:
                        make_visible(gui.get_grid(), cur, vision)
                        gui.update_grid_with_vision()
                        found_flag, last_v, Open, Closed = algorithm(gui.get_grid(), cur, end_pos, OpenGame(your_open), ClosedGame(your_closed), h)
                        if not found_flag:
                            break
                        path = reconstruct_path(last_v)
                        spot = gui.get_spot(cur[0], cur[1])
                        if ((spot.i, spot.j) != start) and ((spot.i, spot.j) != end):
                            pass
                        gui.draw(current=cur, path=path)
                        time.sleep(0.03)
                        cur = path[0]
                        res_path += [cur]
                        if cur == end_pos:
                            s = dict()
                            found_path = []
                            in_cycle = [False] * len(res_path)
                            for i, c in enumerate(res_path):
                                if c in s.keys():
                                    for j in range(s[c], i):
                                        in_cycle[j] = True
                                s[c] = i
                            for n, b in zip(res_path, in_cycle):
                                if not b:
                                    found_path += [n]
                            path_len = len(found_path)
                    

                if event.key == pygame.K_r:
                    start = None
                    end = None
                    found_path = None
                    gui.reset(size, grid_size)
    gui.quit()
