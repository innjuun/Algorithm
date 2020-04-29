
"""
count = 0
while N != 1:
    if N % 3 == 0:
        N = int(N/3)
        count += 1
    elif N % 2 == 0:
        N = int(N/2)
        count += 1
    else:
        N = N-1
        count += 1

print(count)
"""


def go1(n):
    if n == 1:
        return 0
    if d[n] > 0:
        return d[n]
    d[n] = go(n-1) + 1

    if n % 3 == 0:
        temp = go(int(n/3)) + 1
        if d[n] > temp:
            d[n] = temp

    elif n % 2 == 0:
        temp = go(int(n/2)) + 1
        if d[n] > temp:
            d[n] = temp

    return d[n]


def go(n):
    for i in range(2, n+1):
        d[i] = d[i-1]+1
        if (i % 2 == 0 and d[i] > d[i//2] + 1):
            d[i] = d[i//2] + 1
        if (i % 3 == 0 and d[i] > d[i//3] + 1):
            d[i] = d[i//3] + 1

    return d[n]


N = int(input())
d = [0 for i in range(N+1)]

print(go(N))
