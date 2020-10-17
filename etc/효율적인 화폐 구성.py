N, M = map(int, input().split())
li = []
for i in range(N):
    li.append(int(input()))

checked = [9999] * (M + 1)

for l in li:
    checked[l] = 1
m = min(li)
for i in range(m, M):
    if min(checked[i-l] for l in li) != 9999:
        checked[i] = min(checked[i-l] for l in li) + 1
print(checked[M])