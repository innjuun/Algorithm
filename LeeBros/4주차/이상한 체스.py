from copy import deepcopy

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
answer = 10000000

def is_in_grid(i, j):
    return i >= 0 and j >= 0 and i < n and j < m

def go(d, i, j, possible_grid):
    while True:
        next_pos = (i + directions[d % 4][0], j + directions[d % 4][1])
        if is_in_grid(next_pos[0], next_pos[1]):
            possible_grid[next_pos[0]][next_pos[1]] = 0
            if is_counter(next_pos[0], next_pos[1]):
                break
            i, j = next_pos
        else:
            break


def is_counter(i, j):
    return grid[i][j] == 6


def make_check(horse_type, d, i, j, possible_grid):
    possible_grid[i][j] = 0
    if horse_type == 1:
        go(d, i, j, possible_grid)
        
    elif horse_type == 2:
        go(d + 1, i, j, possible_grid)
        go(d + 3, i, j, possible_grid)

    elif horse_type == 3:
        go(d, i, j, possible_grid)
        go(d + 1, i, j, possible_grid)

    elif horse_type == 4:
        go(d, i, j, possible_grid)
        go(d + 1, i, j, possible_grid)
        go(d + 3, i, j, possible_grid)

    elif horse_type == 5:
        go(d, i, j, possible_grid)
        go(d + 1, i, j, possible_grid)
        go(d + 2, i, j, possible_grid)
        go(d + 3, i, j, possible_grid)
                  
  
horse_list = []
counters = []
for i in range(n):
    for j in range(m):
        if grid[i][j] in [1, 2, 3, 4, 5]:
            horse_list.append((grid[i][j], i, j))
        elif grid[i][j] == 6:
            counters.append((i, j))


horse_directions = [0 for _ in range(len(horse_list))]


def make_visited_sum():
    global horse_directions
    possible_grid = [[1 for _ in range(m)] for _ in range(n)]
    for counter in counters:
        possible_grid[counter[0]][counter[1]] = 0

    for index, hd in enumerate(horse_directions):
        make_check(horse_list[index][0], hd, horse_list[index][1], horse_list[index][2], possible_grid)
    return sum(sum(line) for line in possible_grid)


def dfs(index):
    global answer
    if index == len(horse_list):
        answer = min(answer, make_visited_sum())
        return
    for d in range(4):
        horse_directions[index] = d
        dfs(index + 1)


dfs(0)


print(answer)