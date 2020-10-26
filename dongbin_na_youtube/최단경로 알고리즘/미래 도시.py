INF = int(1e9)
N, M = map(int, input().split())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1, N+1):
    graph[i][i] = 0
print(graph)

X, K = map(int, input().split())

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print(graph[1][K] + graph[K][X])