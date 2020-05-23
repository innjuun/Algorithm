from collections import deque

n, m = map(int, input().split())
li = []
for i in range(n):
    li.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

check = [["0"] * m for i in range(n)]
q = deque()
cnt_list = []

"""
def bfs(x, y):
    cnt = 0
    q.append((x, y))
    check[x][y] = li[x][y]
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0 <= nx < n and 0 <= ny < m:
                if li[nx][ny] == li[a][b] and check[nx][ny] == "0":
                    print(cnt)
                    cnt += 1
                    q.append((nx, ny))
                    check[nx][ny] = check[a][b]

                    if cnt == 2:
                        cnt_list.append("Yes")

        cnt = 0
"""


def dfs(x, y, cnt, a, b):
    check[x][y] = li[x][y]
    if cnt >= 4 and x == a and y == b:
        cnt_list.append("Yes")
        return
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m:
            if li[nx][ny] == li[x][y]:

                if check[nx][ny] == "0":
                    continue
                elif li[nx][ny] == li[a][b]:
                    dfs(nx, ny, cnt + 1, a, b)


for i in range(n):
    for j in range(m):
        if check[i][j] == "0":
            dfs(i, j, 1, i, j)

print(cnt_list)
