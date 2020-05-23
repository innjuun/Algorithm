from collections import deque

m, n = map(int, input().split())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
check = [[-1] * m for i in range(n)]
q = deque()


def bfs():
    for i in range(n):
        for j in range(m):
            if li[i][j] == 1:
                q.append((i, j))
                check[i][j] = 0

    while q:

        a, b = q.popleft()

        for i in range(4):

            nx = dx[i] + a
            ny = dy[i] + b
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == -1 and li[nx][ny] == 0:
                    q.append((nx, ny))

                    check[nx][ny] = check[a][b] + 1


for i in range(n):
    for j in range(m):
        if check[i][j] == -1 and li[i][j] == 1:
            pass
bfs()
print(li)
print(check)

ans = 0
for i in range(n):
    for j in range(m):
        if check[i][j] == -1 and li[i][j] == 0:
            ans = -1
            break
        if check[i][j] > ans:
            ans = check[i][j]
    if ans == -1:
        break
print(ans)
