N = int(input())
P = list(map(int, input().split()))
P.sort()
sum = [0] * len(P)
for i in range(len(P)):
    sum[i] = P[i] + sum[i - 1]

real_sum = 0
for i in range(len(P)):
    real_sum += sum[i]

print(real_sum)
