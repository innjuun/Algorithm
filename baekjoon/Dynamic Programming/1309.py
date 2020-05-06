N = int(input())
d = [[0, 0, 0] for i in range(100001)]

d[0][0] = 1
d[0][1] = 1
d[0][2] = 1

d[1][0] = 2
d[1][1] = 2
d[1][2] = 3

for i in range(1, N + 1):
    d[i][2] = (d[i - 1][2] + d[i - 1][1] + d[i - 1][0]) % 9901
    d[i][1] = (d[i - 1][0] + d[i - 1][2]) % 9901
    d[i][0] = (d[i - 1][1] + d[i - 1][2]) % 9901

print((d[N - 1][0] + d[N - 1][1] + d[N - 1][2]) % 9901)
