from collections import deque

cases = int(input())
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

for i in range(cases):

    l = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    q = deque()
    check = [[-1] * l for i in range(l)]

    def bfs(x, y):
        q.append((x, y))
        check[x][y] = 0

        while q:
            t, k = q.popleft()
            for i in range(8):
                nx = t + dx[i]
                ny = k + dy[i]
                if 0 <= nx < l and 0 <= ny < l:
                    if check[nx][ny] == -1:
                        q.append((nx, ny))
                        check[nx][ny] = check[t][k] + 1
                        if nx == c and ny == d:
                            break
            if nx == c and ny == d:
                break

    bfs(a, b)
    print(check[c][d])
