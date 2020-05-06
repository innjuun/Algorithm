N = int(input())

d = [[0 for i in range(10)] for i in range(1001)]

for i in range(10):
    d[1][i] = 1

for i in range(2, 1001):
    for j in range(10):
        for t in range(0, j + 1):
            d[i][j] += d[i - 1][t]
        d[i][j] %= 10007

print(sum(d[N]) % 10007)
