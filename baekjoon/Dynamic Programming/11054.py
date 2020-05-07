N = int(input())

li = list(map(int, input().split()))
d = [1 for i in range(N)]
d2 = [1 for i in range(N)]
for i in range(0, N):

    for j in range(0, i):

        if li[i] > li[j]:
            d[i] = max(d[i], d[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):

        if li[i] > li[j]:
            d2[i] = max(d2[i], d2[j] + 1)


d3 = [0 for i in range(N)]
for i in range(N):
    d3[i] = d[i] + d2[i] - 1

print(max(d3))
