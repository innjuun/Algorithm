import sys
from collections import deque

# sys.setrecursionlimit(100000)
n, m = map(int, input().split())

li = []
for i in range(n):
    li.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

check = [[0] * m for i in range(n)]

"""
def dfs(x, y, count):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if li[nx][ny] == 1 and check[nx][ny] == 0:
                count += 1
                check[nx][ny] = count
                print(count)
                dfs(nx, ny, count)
                count -= 1
                print(check)
"""
count = 1


def bfs(x, y):
    q.append((0, 0))

    check[x][y] = 1

    while q:
        a, b = q.popleft()
        if a == n - 1 and b == m - 1:
            print(check[a][b])
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == 0 and li[nx][ny] == 1:
                    check[nx][ny] = check[a][b] + 1
                    q.append((nx, ny))


q = deque()
bfs(0, 0)


count = 1
