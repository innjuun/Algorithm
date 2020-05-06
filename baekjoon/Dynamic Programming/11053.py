N = int(input())

A = list(map(int, input().split()))
d = [1 for i in range(len(A))]

for i in range(0, len(A)):
    maximum = 1
    for j in range(0, i):
        if A[j] < A[i]:
            d[i] = d[j] + 1
            if maximum < d[i]:
                maximum = d[i]
    d[i] = maximum

print(max(d))
