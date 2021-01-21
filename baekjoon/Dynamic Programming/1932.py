n = int(input())
d = [0]
for i in range(n):
    d.append(list(map(int, input().split())))


for i in range(2, n + 1):
    for j in range(0, i):

        if j == 0:
            d[i][j] = d[i - 1][0] + d[i][j]
        elif j == i - 1:
            d[i][j] = d[i - 1][j - 1] + d[i][j]
        else:
            d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + d[i][j]

print(max(d[n]))
