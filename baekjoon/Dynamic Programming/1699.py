"""
import math


N = int(input())


count = 0
while N != 0:
    N = N - math.floor(math.sqrt(N)) * math.floor(math.sqrt(N))
    count = count + 1

print(count)
"""
"""
import math

N = int(input())

li = [0]
li += [i * i for i in range(380)]
d = [0 for i in range(100001)]

d[1] = li[1]
d[2] = li[1] + li[1]
d[3] = li[1] + li[1] + li[1]
d[4] = li[2]


for i in range(5, 1001):
    maximum = 0
    for j in range(1, math.floor(math.sqrt(i)) + 1):
        maximum = d[j] * d[j] + d[i - j] * d[i - j]
        if maximum > d[i]:
            d[i] = maximum
    print(d)
print(d[N])
"""
"""
n = int(input())
d = [0] * (n + 1)
for i in range(1, n + 1):
    d[i] = i
    j = 1
    while j * j <= i:
        if d[i] > d[i - j * j] + 1:
            d[i] = d[i - j * j] + 1
        j += 1

print(d[n])
"""

n = int(input())
dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    print(s)
    dp[i] = min(s) + 1
print(dp[n])
