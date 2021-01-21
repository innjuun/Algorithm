"""
d += list(0 for i in range(101))

d[1] = 9
d[2] = 17

for i in range(3, 101):
    d[i] = d[i-1] * 2 - (i-1)

print(d[N] % 1000000000)
"""
"""
N = int(input())
d = [0]
d += list([0, 0] for i in range(101))
d[1][0] = 8
d[1][1] = 1
# 2중 인덱스가 0이면 1~8, 2중 인덱스가 1이면 0 or 9

d[2][0] = 15
d[2][1] = 2


for i in range(3, N):
    d[i][0] = d[i-1][0] * 2 + 2
    d[i][1] = d[i-1][1]
print(d)
print(((d[N][0] + d[N][1]) % 1000000000))
"""
mod = 1000000000
N = int(input())
d = [0]
d += [[0 for i in range(10)] for i in range(101)]
for i in range(1, 10):
    d[1][i] = 1
for i in range(2, N + 1):
    for j in range(0, 10):
        d[i][j] = 0
        if j - 1 >= 0:
            d[i][j] += d[i - 1][j - 1]
        if j + 1 < 10:
            d[i][j] += d[i - 1][j + 1]
        d[i][j] = d[i][j] % mod

ans = 0
for i in range(10):
    ans += d[N][i]

print(ans % mod)
