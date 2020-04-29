N = int(input())
card = [0]
card += list(map(int, input().split()))
d = [0 for i in range(N+1)]

d[1] = card[1]
d[2] = max(card[2], card[1]*2)

for i in range(3, N+1):
    d[i] = card[i]
    for j in range(1, i//2+1):
        d[i] = max(d[i], d[j] + d[i-j])

print(d[N])


"""
for i in range(1, N):
    for j in range(1, i):
        d[i] = max(d[i], d[i-j] + li[j])

print(d)
"""
