"""
n = int(input())
li = [[0, 0] for i in range(n + 1)]
for i in range(1, n + 1):
    li[i][1] = int(input())
print(li)
d = [[0, 0] for i in range(n + 1)]

d[1][0] = 0
d[1][1] = li[1]

d[2][0] = li[1]
d[2][1] = li[1] + li[2]

for i in range(3, n + 1):
    d[i][0] = max(
        li[i - 1][1] + li[i - 2][1],
        li[i - 1][0] + li[i - 2][1],
        li[i - 1][0] + li[i - 2][0],
        li[i - 1][1] + li[i - 2][0],
    )
    d[i][1] = (
        max(
            li[i - 1][0] + li[i - 2][1],
            li[i - 1][1] + li[i - 2][0],
            li[i - 1][0] + li[i - 2][0],
        )
        + li[i][1]
    )

print(d)
print(max(d[n][0], d[n][1]))
"""

n = int(input())
a = [0] + [int(input()) for _ in range(n)]
d = [0] * (n + 1)

d[1] = a[1]

if n >= 2:
    d[2] = a[1] + a[2]
for i in range(3, n + 1):
    d[i] = d[i - 1]
    d[i] = max(d[i], d[i - 2] + a[i])
    d[i] = max(d[i], d[i - 3] + a[i] + a[i - 1])
print(d)
print(d[n])
