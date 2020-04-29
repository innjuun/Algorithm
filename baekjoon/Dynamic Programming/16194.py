N = int(input())

li = list(map(int, input().split()))
li.insert(0, 0)

d = [0 for i in range(N+1)]

d[1] = li[1]
d[2] = min(li[1] * 2, li[2])

for i in range(3, N+1):
    d[i] = li[i]
    for j in range(i):
        d[i] = min(d[i], d[i-j] + d[j])

print(d[N])
