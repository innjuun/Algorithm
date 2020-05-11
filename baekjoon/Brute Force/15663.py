n, m = map(int, input().split())

li = list(map(int, input().split()))
a = [0] * m
overlap = []

li.sort()
check = [False] * (n + 1)


def go(index, n, m):

    if index == m:

        if tuple(a) not in overlap:
            overlap.append(tuple(a))
            print(" ".join(map(str, a)))

        return

    for i in range(0, n):
        if check[i]:
            continue
        check[i] = True
        a[index] = li[i]
        go(index + 1, n, m)
        check[i] = False


go(0, n, m)
