n, m = map(int, input().split())
first_status = x, y, d = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
check = [[0 for _ in range(m)] for _ in range(n)]
check[x][y] = 1

NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


d = 10000 + d
curr = [x, y]


def is_visited(i, j):
    return check[i][j]


def is_sidewalk(i, j):
    return grid[i][j]


def is_can_go(i, j):
    return not is_visited(i, j) and not is_sidewalk(i, j)


while True:

    check[curr[0]][curr[1]] = 1
    count = 0
    while count < 4:

        next_position = curr[0] + directions[((d - 1) % 4)][0], curr[1] + directions[(d - 1) % 4][1]
        if is_can_go(next_position[0], next_position[1]):
            d -= 1
            curr = next_position
            break
        else:
            d -= 1
            count += 1
    
    if count == 4:
        backward_position = curr[0] + directions[(d - 2) % 4][0], curr[1] + directions[(d - 2) % 4][1]
        if not is_sidewalk(backward_position[0], backward_position[1]):
            curr = [backward_position[0], backward_position[1]]
        else:
            break

print(sum(sum(line) for line in check))
