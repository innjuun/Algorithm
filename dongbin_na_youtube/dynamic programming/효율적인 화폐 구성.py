N, M = map(int, input().split())
li = []
for i in range(N):
    li.append(int(input()))

checked = [10001] * (M + 1)
checked[0] = 0
for l in li:
    checked[l] = 1
m = min(li)
for i in range(m, M):
    if min(checked[i - l] for l in li) != 10001:
        checked[i] = min(checked[i - l] for l in li) + 1
if checked[M - 1] == 10001:
    print("-1")
print(checked[M - 1])
