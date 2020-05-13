"""
from itertools import combinations


while True:
    case = list(map(int, input().split()))

    if case == [0]:
        break
    else:
        k = case.pop(0)
    li = list(combinations(case, 6))
    for t in li:
        print(" ".join(map(str, t)))

    print()
"""


def go(case, index, start, n, m):

    if index == m:
        print(" ".join(map(str, a)))
        return
    else:
        for i in range(start, n):
            a[index] = case[i]
            go(case, index + 1, i + 1, n, m)
            a[index] = 0


while True:
    case = list(map(int, input().split()))
    if case == [0]:
        break
    else:
        k = case.pop(0)
    case.sort()
    a = [0] * 6
    go(case, 0, 0, k, 6)
    print()
