from collections import deque

n, m, t = map(int, input().split())
graph = [[] for i in range(n + 1)]
check = [False] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for a in graph:
    a.sort()


def dfs(x):
    check[x] = True
    print(x, end=" ")
    for y in graph[x]:
        if check[y] is False:
            dfs(y)


def bfs(start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        y = q.popleft()
        print(y, end=" ")
        for j in graph[y]:
            if check[j] is False:
                check[j] = True
                q.append(j)


dfs(t)
print()
bfs(t)
