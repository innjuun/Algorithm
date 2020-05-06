N = int(input())
li = [0] + list(map(int, input().split()))

d = [1 for i in range(N + 1)]
for i in range(N + 1):
    for j in range(1, i + 1):
        if li[j] > li[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))
