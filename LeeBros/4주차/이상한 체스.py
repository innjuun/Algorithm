from copy import deepcopy

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
answer = 10000000


def is_in_grid(i, j):
    return i >= 0 and j >= 0 and i < n and j < m

def go(d, i, j):
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


def make_check(horse_type, d, i, j):
    possible_grid[i][j] = 0
    if horse_type == 1:
        go(d, i, j)
        
    elif horse_type == 2:
        go(d + 1, i, j)
        go(d + 3, i, j)

    elif horse_type == 3:
        go(d, i, j)
        go(d + 1, i, j)

    elif horse_type == 4:
        go(d, i, j)
        go(d + 1, i, j)
        go(d + 3, i, j)

    elif horse_type == 5:
        go(d, i, j)
        go(d + 1, i, j)
        go(d + 2, i, j)
        go(d + 3, i, j)
                  
  
horse_list = []
counters = []
for i in range(n):
    for j in range(m):
        if grid[i][j] in [1, 2, 3, 4, 5]:
            horse_list.append((grid[i][j], i, j))
        elif grid[i][j] == 6:
            counters.append((i, j))

possible_grid = [[1 for _ in range(m)] for _ in range(n)]
for counter in counters:
    possible_grid[counter[0]][counter[1]] = 0


def dfs(index):
    global answer, possible_grid
    if index == len(horse_list):
        answer = min(answer, sum(sum(line) for line in possible_grid))
        return
    for d in range(4):
        temp_grid = deepcopy(possible_grid)
        make_check(horse_list[index][0], d, horse_list[index][1], horse_list[index][2])
        dfs(index + 1)
        possible_grid = temp_grid


dfs(0)


print(answer)