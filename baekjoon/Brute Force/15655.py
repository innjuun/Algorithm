n, m = map(int, input().split())

li = list(map(int, input().split()))
a = [0] * m
li.sort()


def go(index, selected, n, m):
    if selected == m:
        print(" ".join(map(str, a)))
        return

    if index == n:
        return

    a[selected] = li[index]
    go(index + 1, selected + 1, n, m)

    go(index + 1, selected, n, m)


go(0, 0, n, m)
