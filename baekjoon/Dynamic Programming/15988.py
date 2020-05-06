T = int(input())
mod = 1000000009
li = []
for i in range(T):
    li.append(int(input()))
d = [0 for i in range(1000002)]

d[1] = 1
d[2] = 2
d[3] = 4


for i in li:
    for j in range(4, 1000002):
        d[j] = (d[j - 1] + d[j - 2] + d[j - 3]) % mod


for i in li:
    print(d[i])
