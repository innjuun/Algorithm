import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)


check = [False] * (n)


def dfs(x):
    check[x] = True
    for y in graph[x]:
        if check[y] is False:
            dfs(y)


ans = 0

for i in range(n):
    if check[i] is False:
        dfs(i)
        ans += 1
print(ans)
