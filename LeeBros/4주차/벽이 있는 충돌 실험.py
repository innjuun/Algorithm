T = int(input())
d_map = {
    "U": 0,
    "R": 1,
    "D": 2,
    "L": 3
}
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def is_in_grid(i, j):
    return i >= 0 and j >= 0 and i < n and j < n


def get_grid():
    grid = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        x, y, d = input().split()
        grid[int(x)-1][int(y)-1] = d
    return grid


def swap(alpha):
    if alpha == "U":
        return "D"
    elif alpha == "D":
        return "U"
    elif alpha == "R":
        return "L"
    elif alpha == "L":
        return "R"

    
for _ in range(T):
    marbles = []
    n, m = map(int, input().split())

    grid = get_grid()
    count = 0

    while count < n * 2 + 1:
        next_grid = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] in d_map:
                    next_i, next_j = i + directions[d_map[grid[i][j]]][0], j + directions[d_map[grid[i][j]]][1]
                    if is_in_grid(next_i, next_j):
                        if next_grid[next_i][next_j] != 0:
                            next_grid[next_i][next_j] = 0
                            continue
                        next_grid[next_i][next_j] = grid[i][j]
                    else:
                        if next_grid[i][j] != 0:
                            next_grid[i][j] = 0
                            continue
                        next_grid[i][j] = swap(grid[i][j])
        grid = next_grid
        count += 1
    
    print(sum([sum([1 for g in line if g != 0]) for line in grid]))
        