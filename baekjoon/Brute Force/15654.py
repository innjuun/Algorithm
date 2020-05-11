n, m = map(int, input().split())

li = list(map(int, input().split()))

li.sort()

a = [0] * m
check = [False] * (n)


def go(index, n, m):
    if index == m:
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
