"""https://www.codewars.com/kata/58663693b359c4a6560001d6"""

dirs = {'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}

def maze_runner(maze, directions):
    x, y = 0, 0
    n = len(maze) - 1
    # seek start 
    for num, row in enumerate(maze):
        if 2 in row:
            y, x = num, row.index(2)
    for dir in directions:
        x_mv, y_mv = dirs[dir]
        x += x_mv
        y += y_mv
        if any([x < 0 or x > n, y < 0 or y > n]) or maze[y][x] == 1:
            return 'Dead'
        elif maze[y][x] == 3:
            return 'Finish'
    return 'Lost'
