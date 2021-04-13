import math


def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def is_visible(grid, v, to):
    x1, y1 = v
    x2, y2 = to
    if x1 == x2:
        for i in range(min(y1, y2) + 1, max(y1, y2)):
            if grid.grid[x1][i].is_barrier():
                return False
        return True
    if y1 == y2:
        for i in range(min(x1, x2) + 1, max(x1, x2)):
            if grid.grid[i][y1].is_barrier():
                return False
        return True
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    len = (y2 - y1) / (x2 - x1)
    sign = 1 if (y2 > y1) else -1
    cur = y1
    prev = y1
    #print(x1, y1, x2, y2)
    for i in range(x1, x2):
        cur += len
        next1 = math.floor(cur)
        #print(prev, next1, sign)
        for j in range(prev, next1 + sign, sign):
            if grid.grid[i][j].is_barrier():
                return False
        prev = next1
    return True


def make_visible(grid, pos, radius):
    for i in range(max(0, pos[0] - radius), min(pos[0] + radius + 1, grid.width)):
        for j in range(max(0, pos[1] - radius), min(pos[1] + radius + 1, grid.height)):
            if dist(i, j, pos[0], pos[1]) > radius:
                continue
            if is_visible(grid, pos, (i, j)):
                grid.grid[i][j].make_visible()
