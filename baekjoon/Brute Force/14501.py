N = int(input())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))


li = []


def go(index, m):
    global maximum
    if index == m:

        if sum(li) > maximum:
            maximum = sum(li)
        return

    if index > m:
        return

    li.append(a[index][1])
    go(index + a[index][0], m)
    li.pop()
    go(index + 1, m)


maximum = 0

go(0, N)
print(maximum)
"""
maximum = 0

total = []
tot = []


def go(index, start, n, m):
    if start > m:

        tot.append(sum(total[:-1]))
        return
    if start == m:
        tot.append(sum(total))
        return
    for i in range(start, n):
        total.append(a[i][1])

        go(index + 1, i + a[i][0], n, m)
        total.pop()


go(0, 0, N, N)
print(max(tot))
"""
