N = int(input())
li = []
for i in range(N):
    li.append(list(map(int, input().split())))
d = [[0, 0, 0] for i in range(1001)]

d[0][0] = li[0][0]
d[0][1] = li[0][1]
d[0][2] = li[0][2]

for i in range(N):
    d[i][2] = min(d[i - 1][0] + li[i][2], d[i - 1][1] + li[i][2])
    d[i][1] = min(d[i - 1][2] + li[i][1], d[i - 1][0] + li[i][1])
    d[i][0] = min(d[i - 1][1] + li[i][0], d[i - 1][2] + li[i][0])
print(min(d[N - 1]))
