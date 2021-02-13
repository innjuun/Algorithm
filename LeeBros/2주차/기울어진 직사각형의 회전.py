from copy import deepcopy
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
    for i in range(m1):
        curr = before_curr[0] + direction[0][0], before_curr[1] + direction[0][1]
        grid[before_curr[0]][before_curr[1]] = grid[curr[0]][curr[1]]
        before_curr = curr

    for i in range(m2):
        curr = before_curr[0] + direction[1][0], before_curr[1] + direction[1][1]
        grid[before_curr[0]][before_curr[1]] = grid[curr[0]][curr[1]]
        before_curr = curr
    
    for i in range(m3):
        curr = before_curr[0] + direction[2][0], before_curr[1] + direction[2][1]
        grid[before_curr[0]][before_curr[1]] = grid[curr[0]][curr[1]]
        before_curr = curr
    
    for i in range(m4):
        curr = before_curr[0] + direction[3][0], before_curr[1] + direction[3][1]
        grid[before_curr[0]][before_curr[1]] = grid[curr[0]][curr[1]]
        before_curr = curr
    grid[before_curr[0] - direction[3][0]][before_curr[1] - direction[3][1]] = temp
    

def rotate_reverse(grid, info):
    r, c, m1, m2, m3, m4, dir = info
    r -= 1
    c -= 1

    value = grid[r][c]
    before_curr = r, c

    for i in range(m1):
        curr = before_curr[0] + direction[0][0], before_curr[1] + direction[0][1]
        temp = grid[curr[0]][curr[1]]
        grid[curr[0]][curr[1]] = value
        value = temp
        before_curr = curr

    for i in range(m2):
        curr = before_curr[0] + direction[1][0], before_curr[1] + direction[1][1]
        temp = grid[curr[0]][curr[1]]
        grid[curr[0]][curr[1]] = value
        value = temp
        before_curr = curr

    for i in range(m3):
        curr = before_curr[0] + direction[2][0], before_curr[1] + direction[2][1]
        temp = grid[curr[0]][curr[1]]
        grid[curr[0]][curr[1]] = value
        value = temp
        before_curr = curr

    for i in range(m4):
        curr = before_curr[0] + direction[3][0], before_curr[1] + direction[3][1]
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