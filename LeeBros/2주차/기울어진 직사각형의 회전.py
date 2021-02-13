n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
info = list(map(int, input().split()))

direction = [[-1, 1], [-1, -1], [1, -1], [1, 1]]


def rotate(grid, info):
    r, c, m1, m2, m3, m4, dir = info
    r -= 1
    c -= 1

    temp = grid[r][c]
    before_curr = r, c

    for index, m in enumerate([m1, m2, m3, m4]):
        for _ in range(m):
            curr = before_curr[0] + direction[index][0], before_curr[1] + direction[index][1]
            grid[before_curr[0]][before_curr[1]] = grid[curr[0]][curr[1]]
            before_curr = curr

    grid[before_curr[0] - direction[3][0]][before_curr[1] - direction[3][1]] = temp
    

def rotate_reverse(grid, info):
    r, c, m1, m2, m3, m4, dir = info
    r -= 1
    c -= 1

    value = grid[r][c]
    before_curr = r, c
    for index, m in enumerate([m1, m2, m3, m4]):
        for _ in range(m):
            curr = before_curr[0] + direction[index][0], before_curr[1] + direction[index][1]
            temp = grid[curr[0]][curr[1]]
            grid[curr[0]][curr[1]] = value
            value = temp
            before_curr = curr


if info[-1] == 1:
    rotate(grid, info)
elif info[-1] == 0:
    rotate_reverse(grid, info)

for line in grid:
    for char in line:
        print(char, end=' ')
    print()