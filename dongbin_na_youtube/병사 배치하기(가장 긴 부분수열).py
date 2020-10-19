N = int(input())
li = list(map(int, input().split()))[::-1]

checked = [1 for _ in range(N)]
print(li)
for i in range(N):
    for j in range(i):
        if li[j] < li[i]:
            checked[i] = max(checked[i], checked[j] + 1)
    
print(checked)