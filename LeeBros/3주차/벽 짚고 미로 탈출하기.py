n = int(input())
x, y = list(map(int, input().split()))

curr = [x - 1, y - 1]
answer = 0
grid = [list(input()) for _ in range(n)]

d = 10000
heading = [[0, 1], [-1, 0], [0, -1], [1, 0]]
right_wall = [[1, 0], [0, 1], [-1, 0], [0, -1]]
no_more_wall = [[1, 1], [-1, 1], [-1, -1], [1, -1]]


def is_in_grid(i, j):
    return i >= 0 and j >= 0 and i < n and j < n


def is_wall(i, j):
    
    return is_in_grid(i, j) and grid[i][j] == "#"

first = [x - 1, y - 1]
count = 0
while True:
    count += 1
    if count >= 10000:
        answer = -1
        break
    if is_wall(curr[0] + heading[(d % 4)][0], curr[1] + heading[(d % 4)][1]):
        d += 1
        continue
    
    if is_wall(curr[0] + right_wall[(d % 4)][0], curr[1] + right_wall[(d % 4)][1]):
        if is_in_grid(curr[0] + heading[(d % 4)][0], curr[1] + heading[(d % 4)][1]):
            if is_wall(curr[0] + no_more_wall[(d % 4)][0], curr[1] + no_more_wall[(d % 4)][1]):
                answer += 1
                curr = [curr[0] + heading[(d % 4)][0], curr[1] + heading[(d % 4)][1]]
            else:
                answer += 2
                curr = [curr[0] + no_more_wall[(d % 4)][0], curr[1] + no_more_wall[(d % 4)][1]]
                d -= 1
        else:
            answer += 1
            break



print(answer)
