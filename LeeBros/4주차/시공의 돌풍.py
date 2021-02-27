from copy import deepcopy


n, m, t = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def find_wind(grid):
    for i in range(len(grid)):
        if grid[i][0] == -1:
            return i, 0

        
wind_up = find_wind(grid)
wind_down = (wind_up[0] + 1, wind_up[1])


def is_in_grid(i, j):
    return i >= 0 and j >= 0 and i < n and j < m


def is_valid_grid(i, j):
    return is_in_grid(i, j) and (i, j) != wind_up and (i, j) != wind_down


def spread(grid):
    new_grid = deepcopy(grid)
    
    for i in range(n):
        for j in range(m):
            if is_valid_grid(i, j):
                for d in directions:
                    value = grid[i][j] // 5
                    if is_valid_grid(i + d[0], j + d[1]):
                        new_grid[i + d[0]][j + d[1]] += value
                        new_grid[i][j] = new_grid[i][j] - value
            
    return new_grid


def rotate(grid):
    new_grid = deepcopy(grid)
    rotate_up(new_grid)
    rotate_down(new_grid)
    return new_grid


def rotate_up(grid):
    order = (1, 0, 3, 2)
    i, j = wind_up
    cnt = 0
    value = 0
    while True:
        if cnt == 4:
            break
        next_i, next_j = i + directions[order[cnt]][0], j + directions[order[cnt]][1]
        if not is_valid_grid(next_i, next_j):
            cnt += 1
            continue
        temp = grid[next_i][next_j]
        grid[next_i][next_j] = value
        value = temp
        i, j = next_i, next_j


def rotate_down(grid):
    order = (1, 2, 3, 0)
    i, j = wind_down
    cnt = 0
    value = 0
    while True:
        if cnt == 4:
            break
        next_i, next_j = i + directions[order[cnt]][0], j + directions[order[cnt]][1]
        if not is_valid_grid(next_i, next_j):
            cnt += 1
            continue
        temp = grid[next_i][next_j]
        grid[next_i][next_j] = value
        value = temp
        i, j = next_i, next_j


for time in range(t):
    # print(grid)
    spreaded = spread(grid)
    # print(spreaded)
    grid = rotate(spreaded)

print(sum(sum(line) for line in grid) + 2)
