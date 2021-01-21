N, K = map(int, input().split())
count = 0
coin_list = [0] * 10
for i in range(N):
    coin_list[i] = int(input())
for j in range(N - 1, -1, -1):
    if coin_list[j] <= K:
        count = count + (K // coin_list[j])
        K = K % coin_list[j]


print(count)
