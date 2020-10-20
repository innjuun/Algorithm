import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())


graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for node, edge in graph[now]:
            cost = dist + edge
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
                
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
