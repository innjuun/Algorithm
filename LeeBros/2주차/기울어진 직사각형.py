n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0
direction = [[-1, 1], [-1, -1], [1, -1], [1, 1]]


def is_valid(i, j):
    return i >= 0 and j >= 0 and i < n and j < n


def add_all(grid, i, j, k, l):
    curr = i, j
    total = 0
    for idx, cnt in enumerate([k, l, k, l]):
        for _ in range(cnt + 1):
            if not is_valid(curr[0] + direction[idx][0], curr[1] + direction[idx][1]):
                return False
            curr = curr[0] + direction[idx][0], curr[1] + direction[idx][1]
            total += grid[curr[0]][curr[1]]
    return total


for i in range(n):
    for j in range(n):
        for k in range(n-2):
            for l in range(n-2):
                result = add_all(grid, i, j, k, l)
                answer = max(answer, result) if result else answer

print(answer)
