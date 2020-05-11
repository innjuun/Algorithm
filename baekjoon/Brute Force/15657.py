n, m = map(int, input().split())

li = list(map(int, input().split()))
a = [0] * m
li.sort()


def go(index, start, n, m):
    if index == m:
        print(" ".join(map(str, a)))
        return
    for i in range(start, n):

        a[index] = li[i]
        go(index + 1, i, n, m)


go(0, 0, n, m)
