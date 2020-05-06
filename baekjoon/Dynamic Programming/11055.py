N = int(input())

li = [0] + list(map(int, input().split()))

d = [0 for i in range(N + 1)]


for i in range(1, N + 1):
    for j in range(i + 1):
        if li[j] < li[i]:
            d[i] = max(d[i], d[j] + li[i])


print(max(d))
