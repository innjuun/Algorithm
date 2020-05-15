n, m = map(int, input().split())
li = []
for i in range(n):
    li.append(list(map(int, input())))
ans = 0
for s in range(1 << (n * m)):
    sum = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i * m + j
            if (s & (1 << k)) == 0:
                cur = 10 * cur + li[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i * m + j
            if (s & (1 << k)) != 0:
                cur = 10 * cur + li[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    ans = max(ans, sum)

print(ans)
