n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append([])
    nums = list(input().split())
    for num in nums:
        grid[-1].append([num])
moves = list(map(int, input().split()))


def find_num_position(target):
    for i in range(n):
        for j in range(n):
            for k, num in enumerate(grid[i][j]):
                if num == str(target):
                    return i, j, k


def is_in_grid(i, j):
    return i >= 0 and j >= 0 and i < n and j < n


def find_max_position(i, j):
    max_pos = (-1, -1)
    maximum = 0
    for k in range(3):
        for t in range(3):
            if k == 1 and t == 1:
                continue
            if is_in_grid(i - 1 + k, j - 1 + t):
                for num in grid[i - 1 + k][j - 1 + t]:
                    if int(num) > maximum:
                        maximum = int(num)
                        max_pos = (i - 1 + k, j - 1 + t)
    
    return max_pos


for move in moves:
    i, j, k = find_num_position(move)
    next_i, next_j = find_max_position(i, j)
    if next_i == -1 and next_j == -1:
        continue

    popped = grid[i][j][k:]
    grid[i][j] = grid[i][j][:k]

    grid[next_i][next_j] += popped
    

for i in range(n):
    for j in range(n):
        if grid[i][j]:
            print(' '.join(reversed(grid[i][j])))
        else:
            print("None")