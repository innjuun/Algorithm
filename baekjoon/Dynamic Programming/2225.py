N, K = map(int, input().split())
mod = 1000000000
d = [[0 for i in range(N + 1)] for j in range(K + 1)]
d[0][0] = 1

for i in range(1, K + 1):
    for j in range(0, N + 1):
        for l in range(0, j + 1):
            d[i][j] += d[i - 1][j - l]
        d[i][j] %= mod
print(d)
print(d[K][N])
