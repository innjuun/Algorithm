from copy import deepcopy


NORTH, SOUTH = 0, 1
ROTATE, REVERSE = 1, -1
grid = [list(map(int, list(input()))) for _ in range(4)]
k = int(input())
tries = [list(map(int, input().split())) for _ in range(k)]


def rotate(line, d):
    ret = deepcopy(line)
    if d == ROTATE:
        ret.insert(0, ret.pop())
    elif d == REVERSE:
        ret.append(ret.pop(0))
    return ret


for t in tries:
    new_grid = deepcopy(grid)
    n, d = t
    n -= 1

    new_grid[n] = rotate(grid[n], d)
    temp_n = n
    temp_d = d
    while n + 1 <= 3:
        if grid[n][2] != grid[n + 1][6]:
            d = -d
            new_grid[n + 1] = rotate(grid[n + 1], d)
        else:
            break
        n += 1

    n = temp_n
    d = temp_d
    while n - 1 >= 0:
        if grid[n][6] != grid[n - 1][2]:
            d = -d
            new_grid[n - 1] = rotate(grid[n - 1], d)
        else:
            break
        n -= 1

    grid = deepcopy(new_grid)

print(grid[0][0] + 2*grid[1][0] + 4*grid[2][0] + 8*grid[3][0])