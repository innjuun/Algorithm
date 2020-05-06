n = int(input())

li = list(map(int, input().split()))

d = [0 for i in range(n)]
for i in range(n):
    d[i] = li[i]
    if d[i - 1] + d[i] > d[i]:
        d[i] = d[i - 1] + d[i]

print(max(d))
