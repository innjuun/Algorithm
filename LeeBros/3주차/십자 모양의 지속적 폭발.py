from copy import deepcopy
n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

cols = [int(input()) - 1 for _ in range(m)]


def get_top_pos(grid, col):
    for i in range(n):
        if grid[i][col] != 0:
            return i, col
    return -1, -1


def is_in_grid(i, j):
    return i >= 0 and j >= 0 and i < n and j < n


def make_zeros(grid, i, j):
    ret = deepcopy(grid)
    scope = grid[i][j]
    for k in range(i - scope + 1, i + scope):
        if is_in_grid(k, j):
            ret[k][j] = 0
    
    for l in range(j - scope + 1, j + scope):
        if is_in_grid(i, l):
            ret[i][l] = 0
    
    return ret


def drop(grid):
    ret = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        k = n - 1
        for i in range(n-1, -1, -1):
            if grid[i][j] != 0:
                ret[k][j] = grid[i][j]
                k -= 1
    
    return ret

for col in cols:
    pos = get_top_pos(grid, col)
    if pos == (-1, -1):
        continue
    grid = make_zeros(grid, pos[0], pos[1])
    grid = drop(grid)
    
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
        