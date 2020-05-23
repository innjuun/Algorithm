from collections import deque

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]
cnt_list = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    li = []
    for i in range(h):
        li.append(list(map(int, input().split())))

    q = deque()
    check = [[False] * w for i in range(h)]

    def bfs(x, y):
        q.append((x, y))
        check[x][y] = True
        while q:
            a, b = q.popleft()
            for i in range(8):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if li[nx][ny] == 1 and check[nx][ny] is False:
                        q.append((nx, ny))
                        check[nx][ny] = True

    cnt = 0
    for i in range(h):
        for j in range(w):
            if li[i][j] == 1 and check[i][j] is False:
                cnt += 1
                bfs(i, j)
    cnt_list.append(cnt)


for ans in cnt_list:
    print(ans)
