from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

def draw(gridMap, start=None, goal=None, path=None, nodesExpanded=None, nodesOpened=None):
    k = 5
    hIm = gridMap.grid.height * k
    wIm = gridMap.grid.width * k
    im = Image.new('RGB', (wIm, hIm), color='white')
    draw = ImageDraw.Draw(im)
    for i in range(gridMap.grid.height):
        for j in range(gridMap.grid.width):
            if (gridMap.grid.cells[i][j] == 1):
                draw.rectangle((j * k, i * k, (j + 1) * k - 1, (i + 1) * k - 1), fill=(70, 80, 80))

    if nodesOpened is not None:
        for node in nodesOpened:
            draw.rectangle((node.j * k, node.i * k, (node.j + 1) * k - 1, (node.i + 1) * k - 1), fill=(213, 219, 219),
                           width=0)

    if nodesExpanded is not None:
        for node in nodesExpanded:
            draw.rectangle((node.j * k, node.i * k, (node.j + 1) * k - 1, (node.i + 1) * k - 1), fill=(131, 145, 146),
                           width=0)

    if path is not None:
        for step in path:
            if (step is not None):
                if (gridMap.grid.traversable(step.i, step.j)):
                    draw.rectangle((step.j * k, step.i * k, (step.j + 1) * k - 1, (step.i + 1) * k - 1),
                                   fill=(52, 152, 219), width=0)
                else:
                    draw.rectangle((step.j * k, step.i * k, (step.j + 1) * k - 1, (step.i + 1) * k - 1),
                                   fill=(230, 126, 34), width=0)

    if (start is not None) and (gridMap.grid.traversable(start.i, start.j)):
        draw.rectangle((start.j * k, start.i * k, (start.j + 1) * k - 1, (start.i + 1) * k - 1), fill=(40, 180, 99),
                       width=0)

    if (goal is not None) and (gridMap.grid.traversable(goal.i, goal.j)):
        draw.rectangle((goal.j * k, goal.i * k, (goal.j + 1) * k - 1, (goal.i + 1) * k - 1), fill=(231, 76, 60),
                       width=0)

    fig, ax = plt.subplots(dpi=150)
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    plt.imshow(np.asarray(im))
