"""import sys

N, M = map(int, input().split())

c = [False for i in range(N + 1)]
a = [0 for i in range(M)]


def go(index, n, m):
    if index == m:
        print(" ".join(map(str, a)))
        return
    for i in range(1, n + 1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index + 1, n, m)
        c[i] = False


go(0, N, M)
"""


n, m = map(int, input().split())

check = [False] * (n + 1)
a = [0] * m


def go(index, n, m):
    if index == m:
        for char in a:
            print(char, end=" ")
        print()
        return

    for i in range(1, n + 1):
        if i in a:
            continue

        a[index] = i

        go(index + 1, n, m)

        a[index] = 0


go(0, n, m)
