"""
import sys

n, m = map(int, input().split())


edges = []
am = [[False] * n for _ in range(n)]
al = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))
    edges.append((b, a))
    am[a][b] = True
    am[b][a] = True
    al[a].append(b)
    al[b].append(a)
m *= 2

for i in range(m):
    for j in range(m):
        A, B = edges[i]
        C, D = edges[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not am[B][C]:
            continue
        for E in al[D]:
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            sys.exit(0)

print(0)
"""
import sys

n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


check = [False] * n

result = False


def dfs(now, depth):
    global result

    if depth == 5:
        result = True
        return

    for nextt in graph[now]:

        if check[nextt] is False:
            check[nextt] = True

            dfs(nextt, depth + 1)
            check[nextt] = False


for i in range(n):
    check[i] = True
    dfs(i, 1)

    if result is True:
        print("1")
        sys.exit(0)
    check[i] = False
print("0")
