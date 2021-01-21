import heapq


N, M, C = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


heap = []
distance = [INF] * (N + 1)
heapq.heappush(heap, (0, C))
distance[C] = 0
while heap:
    dist, now = heapq.heappop(heap)
    if dist > distance[now]:
        continue
    for node, edge in graph[now]:
        if dist + edge < distance[node]:
            heapq.heappush(heap, (dist, node))
            distance[node] = dist + edge

city = 0
maximum = 0
for i in range(1, len(distance)):
    if distance[i] != 0 and distance[i] != INF:
        maximum = max(maximum, distance[i])
        city += 1

print(city, maximum)
