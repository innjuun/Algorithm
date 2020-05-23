import sys

sys.setrecursionlimit(100000)


def dfs(x, num):

    check[x] = num

    for y in graph[x]:
        if check[y] == 0:

            dfs(y, 3 - num)


k = int(input())


for i in range(k):
    v, e = map(int, input().split())
    check = [0] * v
    graph = [[] for i in range(v)]

    for i in range(e):
        u, t = map(int, input().split())
        graph[u - 1].append(t - 1)
        graph[t - 1].append(u - 1)

    for i in range(len(graph)):
        if check[i] == 0:
            dfs(i, 1)

    result = True
    for i in range(len(graph)):
        for j in graph[i]:
            if check[j] == check[i]:
                result = False
    if result is True:
        print("YES")
    else:
        print("NO")
