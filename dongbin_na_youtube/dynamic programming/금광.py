T = int(input())
result = []
for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    checked = [[0] * m for _ in range(n)]
    # checked = []
    # index = 0
    # for i in range(n):
    #     checked.append(a[index:index+m])
    #     index += m
    for i in range(len(a)):
        checked[(i // m)][(i % m)] = a[i]
    
    for j in range(1, m):
        for i in range(n):
            tmp = checked[i][j-1]
            if i > 0:
                tmp = max(tmp, checked[i-1][j-1])
            if i < n -1:
                tmp = max(tmp, checked[i+1][j-1])
            checked[i][j] = max(tmp + checked[i][j], checked[i][j])

print(max([i[-1] for i in checked] q    ))