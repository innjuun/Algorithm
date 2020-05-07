N = int(input())
li = []
for i in range(N):
    li.append(list(map(int, input().split())))


d = [[0, 0, 0] for i in range(N)]

ans = 10000000000
for k in range(0, 3, 1):
    for j in range(0, 3, 1):
        if j == k:
            d[0][j] = li[0][j]
            continue
        d[0][j] = 10000000000

    for i in range(1, N):
        d[i][0] = li[i][0] + min(d[i - 1][1], d[i - 1][2])
        d[i][1] = li[i][1] + min(d[i - 1][0], d[i - 1][2])
        d[i][2] = li[i][2] + min(d[i - 1][0], d[i - 1][1])

    for j in range(0, 3, 1):
        if j == k:
            continue
        ans = min(ans, d[N - 1][j])
        print(d)

print(ans)
