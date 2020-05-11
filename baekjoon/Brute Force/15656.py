n, m = map(int, input().split())

li = list(map(int, input().split()))
a = [0] * m
li.sort()


def go(index, n, m):
    if index == m:
        print(" ".join(map(str, a)))
        return
    for i in range(0, n):
        a[index] = li[i]
        go(index + 1, n, m)


go(0, n, m)
