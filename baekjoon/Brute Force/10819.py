from itertools import permutations

n = int(input())

A = list(map(int, input().split()))
li = list(permutations(A))


real_max = 0
for a in li:
    max = 0
    for i in range(n - 1):
        max += abs(a[i] - a[i + 1])

    if real_max < max:
        real_max = max
print(real_max)
