T = int(input())
result = []
for test in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    li = list(zip(A, B))

    d = [[0, 0, 0] for i in range(100001)]
    d[0][0] = li[0][0]
    d[0][1] = li[0][1]
    d[0][2] = 0
    for i in range(1, n):
        d[i][0] = max(d[i - 1][1], d[i - 1][2]) + li[i][0]
        d[i][1] = max(d[i - 1][0], d[i - 1][2]) + li[i][1]
        d[i][2] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2])

    result.append(max(d[n - 1]))

for res in result:
    print(res)
