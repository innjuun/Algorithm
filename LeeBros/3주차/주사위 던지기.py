n ,m, r, c = map(int, input().split())

curr = [r - 1, c - 1]

LEFT, RIGHT, UP, DOWN = 'L', 'R', 'U', 'D'

moves = list(input().split())
status = [2, 3, 1, 5, 4, 6]
grid = [[0 for _ in range(n)] for _ in range(n)] 


def is_in_grid(i, j):
    return i >= 0 and j >= 0 and i < n and j < n


def get_next(curr, move):
    if move == LEFT:
        return [curr[0], curr[1] - 1]
    elif move == RIGHT:
        return [curr[0], curr[1] + 1]
    elif move == UP:
        return [curr[0] - 1, curr[1]]
    elif move == DOWN:
        return [curr[0] + 1, curr[1]]


def tilt(status, move):
    if move == LEFT:
        return [status[0], status[5], status[1], status[3], status[2], status[4]]
    elif move == RIGHT:
        return [status[0], status[2], status[4], status[3], status[5], status[1]]
    elif move == UP:
        return [status[5], status[1], status[0], status[2], status[4], status[3]]
    elif move == DOWN:
        return [status[2], status[1], status[3], status[5], status[4], status[0]]

    
def get_total(grid):
    return sum(sum(line) for line in grid)


grid[curr[0]][curr[1]] = status[5]


for move in moves:
    next_x, next_y = get_next(curr, move)
    if not is_in_grid(next_x, next_y):
        pass
    else:
        curr = next_x, next_y
        status = tilt(status, move)

    grid[curr[0]][curr[1]] = status[5]


print(get_total(grid))

    