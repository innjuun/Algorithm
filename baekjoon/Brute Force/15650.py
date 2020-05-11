"""
n, m = map(int, input().split())
check = [False] * (n + 1)
a = [0] * m


def go(index, start, n, m):
    if index == m:
        print(" ".join(map(str, a)))
        return
    for i in range(start, n + 1):

        a[index] = i

        go(index + 1, i + 1, n, m)

        a[index] = 0


go(0, 1, n, m)
"""
"""
n, m = map(int, input().split())
check = [False] * (n + 1)
a = [0] * m


def go(index, n, m):
    if index == m:
        print(" ".join(map(str, a)))
        return
    for i in range(a[index - 1] + 1, n + 1):
        print(a)
        a[index] = i

        go(index + 1, n, m)

        a[index] = 0


go(0, n, m)

"""
import sys

n, m = map(int, input().split())
a = [0] * m


def go(index, selected, n, m):
    if selected == m:
        sys.stdout.write(" ".join(map(str, a)) + "\n")
        return
    if index > n:
        return
    a[selected] = index

    go(index + 1, selected + 1, n, m)

    a[selected] = 0
    go(index + 1, selected, n, m)


go(1, 0, n, m)
