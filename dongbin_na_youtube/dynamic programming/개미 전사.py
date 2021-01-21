N = int(input())

K = list(map(int, input().split()))

checked = [0] * N

checked[0] = K[0]
checked[1] = K[1]

for i in range(2, N):
    checked[i] = max(checked[i - 2] + K[i], checked[i - 1])

print(checked)
