dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, count):
    group[x][y] = count

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if li[nx][ny] == 1 and group[nx][ny] == 0:

                dfs(nx, ny, count)


n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input())))

group = [[0] * n for i in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if li[i][j] == 1 and group[i][j] == 0:

            count += 1
            dfs(i, j, count)

maximum = 0
for i in range(n):
    for j in range(n):
        if group[i][j] > maximum:
            maximum = group[i][j]
print(maximum)
cnt = 0
cnt_list = []
for i in range(1, maximum + 1):
    for t in range(n):
        cnt += group[t].count(i)
    cnt_list.append(cnt)
    cnt = 0

cnt_list.sort()
for cnt in cnt_list:
    print(cnt)
