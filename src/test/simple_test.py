import math

from src.test.draw import draw
from src.test.map import Map


class Node:
    def __init__(self, i, j, g=math.inf, h=math.inf, parent=None):
        self.i = i
        self.j = j
        self.g = g
        self.f = self.g + h
        self.parent = parent

    def __eq__(self, other):
        return (self.i == other.i) and (self.j == other.j)

    def __gt__(self, other):
        return self.f > other.f

    def __hash__(self):
        return 31 + 7 * (hash(self.i) + 7 * hash(self.j))

    def __str__(self):
        return 'i: {0}, j: {1}, g: {2}, F: {3}, parent: {4}'.format(self.i, self.j, self.g, self.f, self.parent)


class Grid:

    def __init__(self, height=0, width=0, cells=[]):
        self.height = height
        self.width = width
        self.cells = cells

    # Проверка, не выходит ли клетка (i, j) за границы поля
    def in_bounds(self, i, j):
        return (0 <= j < self.width) and (0 <= i < self.height)

    # Проверка, можно ли пройти через клетку (i, j)
    def traversable(self, i, j):
        return not self.cells[i][j]

    # Список соседей клетки (i, j) в виде list-а из tuple-ов вида (n_i, n_j)
    def get_neighbors(self, i, j):
        neighbors = []
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for d in delta:
            if self.in_bounds(i + d[0], j + d[1]) and self.traversable(i + d[0], j + d[1]):
                neighbors.append((i + d[0], j + d[1]))

        return neighbors

def MakePath(goal):
    length = goal.g
    current = goal
    path = []
    while current.parent:
        path.append(current)
        current = current.parent
    path.append(current)
    return path[::-1], length

def draw_test_map():
    g = Grid()
    m = Map(Grid())
    height = 15
    width = 30
    mapstr = '''
    . . . . . . . . . . . . . . . . . . . . . # # . . . . . . .  
    . . . . . . . . . . . . . . . . . . . . . # # . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . # # . . . . . . . 
    . . . # # . . . . . . . . . . . . . . . . # # . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . # # . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . # # # # # . . . . 
    . . . # # . . . . . . . . # # . . . . . . # # # # # . . . . 
    . . . # # . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . # # . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . # # . . . . . . . . . . . . . . .'''

    m.ReadFromString(mapstr, width, height)
    start = Node(1, 1)
    goal = Node(13, 28)
    draw(m, start, goal)

def simple_test(algo, Open, Closed, Grid, h):
    open = Open()
    closed = Closed()
    height = 15
    width = 30
    mapstr = '''
    . . . . . . . . . . . . . . . . . . . . . # # . . . . . . .  
    . . . . . . . . . . . . . . . . . . . . . # # . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . # # . . . . . . . 
    . . . # # . . . . . . . . . . . . . . . . # # . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . # # . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . # # # # # . . . . 
    . . . # # . . . . . . . . # # . . . . . . # # # # # . . . . 
    . . . # # . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . # # . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . # # . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . # # . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . # # . . . . . . . . . . . . . . .'''

    grid = Grid()
    taskMap = Map(grid)
    taskMap.ReadFromString(mapstr, width, height)
    start = Node(1, 1)
    goal = Node(13, 28)
    realLen = 39

    try:
        flag, endN = algo(grid, (start.i, start.j), (goal.i, goal.j), open, closed, h)
        nodesExpanded = closed
        nodesOpened = open
        if flag:
            path = MakePath(endN)
            correct = abs(path[1] - realLen) == 0
            print("Path found! Length: " + str(path[1]) + ". Nodes created: " + str(
                len(nodesOpened) + len(nodesExpanded)) + ". Number of steps: " + str(
                len(nodesExpanded)) + ". Correct: " + str(correct))
            draw(taskMap, start, goal, path[0], nodesExpanded, nodesOpened)
        else:
            print("Path not found!")
            draw(taskMap, start, goal, None, nodesExpanded, nodesOpened)
    except Exception as e:
        print("Execution error")
        print(e)