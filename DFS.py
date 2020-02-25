def drawmaze(maze):
    symbols = " #x."
    for line in maze:
        for cell in line:
            print(symbols[cell], end="")
        print()


UNVISITED = 0
IN_PROGRESS = 3
EXIT = 2
WALL = 1


def get_adyacencies(maze, node):
    adyacencies = []

    x = node[0]
    y = node[1]

    if x < (len(maze) - 1):
        if maze[x + 1][y] != WALL:
            adyacencies.append((x + 1, y))
    if x > 0 and maze[x-1][y] != WALL:
        adyacencies.append((x-1,y))

    if y > 0 and maze[x][y-1]!= WALL:
        adyacencies.append((x,y-1))

    if y < (len(maze) - 1) and maze[x][y +  1] != WALL:
        adyacencies.append((x, y + 1))
    return adyacencies

# 0 Available cell
# 1 Wall
# 2 Exit
# 3 In progress
maze = [[0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 2],
        [1, 1, 0, 0, 0, 1]]
start = (0, 0)


def dfs(maze, start):
    # ROW      COLUMN
    if maze[start[0]][start[1]] == EXIT:
        print('you did it bro')
        drawmaze(maze)
        return

    maze[start[0]][start[1]] = IN_PROGRESS
    for ady in get_adyacencies(maze, start):
        if maze[ady[0]][ady[1]] == UNVISITED or maze[ady[0]][ady[1]] == EXIT:
            dfs(maze, ady)


drawmaze(maze)
dfs(maze, start)
