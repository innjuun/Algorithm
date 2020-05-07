"""
n = int(input())

li = [0] + list(map(int, input().split()))
d = [0 for i in range(n + 1)]
k = []
for i in range(0, n):
    d = [0 for i in range(n + 1)]
    value = li.pop(i)
    for j in range(1, n):
        d[j] = max(d[j - 1] + li[j], d[j])

    k.append(max(d))
    li.insert(i, value)


print(max(k))
"""

n = int(input())

li = list(map(int, input().split()))

d1 = [0 for i in range(n)]
d2 = [0 for i in range(n)]
d1[0] = li[0]
for i in range(1, n):
    d1[i] = max(li[i], d1[i - 1] + li[i])


d2[n - 1] = li[n - 1]
for i in range(n - 2, -1, -1):
    d2[i] = max(li[i], d2[i + 1] + li[i])


d3 = [0 for i in range(n)]

d3[0] = li[0]
d3[n - 1] = li[n - 1]


for i in range(1, n - 1):
    d3[i] = d1[i - 1] + d2[i + 1]


print(d1)
print(d2)
print(d3)

print(max(max(d1), max(d3)))
