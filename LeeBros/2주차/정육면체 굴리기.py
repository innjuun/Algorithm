
n, m, x, y, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

EAST, WEST, NORTH, SOUTH = 1, 2, 3, 4
directions = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]

ways = list(map(int, input().split()))

FRONT, RIGHT, UP = 0, 1, 2

sides = [0, 0, 0, 0, 0, 0]


def is_valid_grid(i, j):
    return i >= 0 and j >= 0 and i < n and j < m


def move(sides, way, grid, curr):
    first, second, third, sixth, fifth, fourth = sides
    if way == EAST:
        new_sides = [first, third, fifth, sixth, fourth, second]
    elif way == WEST:
        new_sides = [first, fourth, second, sixth, third, fifth]
    elif way == NORTH:
        new_sides = [fourth, second, first, third, fifth, sixth]
    elif way == SOUTH:
        new_sides = [third, second, sixth, fourth, fifth, first]

    if grid[curr[0]][curr[1]] == 0:
        grid[curr[0]][curr[1]] = new_sides[5]
    else:
        new_sides[5] = grid[curr[0]][curr[1]]
        grid[curr[0]][curr[1]] = 0
    return new_sides


curr = x, y


for way in ways:
    if not is_valid_grid(curr[0] + directions[way][0], curr[1] + directions[way][1]):
        continue
    curr = curr[0] + directions[way][0], curr[1] + directions[way][1]
    sides = move(sides, way, grid, curr)
    print(sides[2])
