class Map:

    # Default constructor
    def __init__(self, grid):
        self.width = grid.width
        self.height = grid.height
        self.grid = grid

    # Converting a string (with '#' representing obstacles and '.' representing free cells) to a grid
    def ReadFromString(self, cellStr, width, height):
        self.grid.width = width
        self.width = width
        self.grid.height = height
        self.height = height
        self.grid.cells = [[0 for _ in range(width)] for _ in range(height)]
        cellLines = cellStr.split("\n")
        i = 0
        j = 0
        for l in cellLines:
            if len(l) != 0:
                j = 0
                for c in l:
                    if c == '.':
                        self.grid.cells[i][j] = 0
                    elif c == '#':
                        self.grid.cells[i][j] = 1
                    else:
                        continue
                    j += 1
                # TODO
                if j != width:
                    raise Exception("Size Error. Map width = ", j, ", but must be", width, "kek", i)

                i += 1

        if i != height:
            raise Exception("Size Error. Map height = ", i, ", but must be", height)

    # Initialization of map by list of cells.
    def SetGridCells(self, width, height, gridCells):
        self.grid.width = width
        self.width = width
        self.grid.height = height
        self.height = height
        self.grid.cells = gridCells