from copy import deepcopy
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

UP, DOWN, LEFT, RIGHT = directions = [0, 1, 2, 3]
answer = 0


def reverse_grid(grid):
    ret = deepcopy(grid)
    for i in range(n):
        for j in range(i + 1, n):
            ret[i][j], ret[j][i] = ret[j][i], ret[i][j]
    return ret


def left_merge(row):
    row = [i for i in row if i != 0]
    ret = []

    while row:
        item = row.pop(0)
        if ret and ret[-1] == item:
            ret.append(ret.pop() + item)
        else:
            ret.append(item)

    zeros = n - len(ret)
    for _ in range(zeros):
        ret.append(0)

    return ret


def right_merge(row):
    row = [i for i in row if i != 0]
    ret = []
    
    while row:
        item = row.pop()
        if ret and ret[0] == item:
            ret.insert(0, ret.pop(0) + item)
        else:
            ret.insert(0, item)

    zeros = n - len(ret)
    for _ in range(zeros):
        ret.insert(0, 0)

    return ret


def move(index, grid, direction):
    global answer

    ret = []
    if direction == LEFT:
        for i in range(n):
            ret.append(left_merge(grid[i]))

    elif direction == RIGHT:
        for i in range(n):
            ret.append(left_merge(grid[i]))

    elif direction == UP:
        reversed_grid = reverse_grid(grid)
        for i in range(n):
            ret.append(left_merge(reversed_grid[i]))

        ret = reverse_grid(ret)

    elif direction == DOWN:
        reversed_grid = reverse_grid(grid)
        for i in range(n):
            ret.append(right_merge(reversed_grid[i]))

        ret = reverse_grid(ret)

    if index == 4:
        answer = max(answer, max([max(line) for line in ret]))
        # print(answer)
    return ret


def dfs(index, grid):
    if index == 5:
        return
    for direction in directions:
        next_grid = move(index, grid, direction)
        dfs(index + 1, next_grid)


dfs(0, array)

print(answer)
