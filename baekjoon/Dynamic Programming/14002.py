"""
N = int(input())

A = list(map(int, input().split()))
d = [1 for i in range(len(A) + 1)]
route = [[0] for i in range(len(A) + 1)]
for i in range(0, len(A)):
    max_route = [A[i]]
    route[i][0] = A[i]
    for j in range(0, i):
        if A[i] > A[j] and d[i] < d[j] + 1:

            d[i] = d[j] + 1
            if len(route[j]) + len(route[i]) > len(max_route):
                max_route = route[j] + route[i]
    route[i] = max_route


maximum = []
for a in route:

    if len(a) > len(maximum):
        maximum = a
print(len(maximum))
for i in maximum:
    print(i, end=" ")
"""
n = int(input())
a = list(map(int, input().split()))

d = [0] * n
v = [-1] * n

for i in range(n):
    d[i] = 1
    for j in range(i):

        if a[j] < a[i] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1
            v[i] = j

ans = max(d)

p = [i for i, x in enumerate(d) if x == ans][0]
print(v)
print(ans)


def go(p):
    if p == -1:
        return
    go(v[p])
    print(a[p], end=" ")


go(p)
print()
