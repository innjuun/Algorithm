from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v+1)

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    indegree[b] += 1
    
def topology_sort():
    result = []
    
    q = deque()
    
    for i in range(1, len(indegree)+1):
        if indegree[i] == 0:
            q.append(indegree[i])
    
    while q:
        node = q.popleft()
        result.append(node)
        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')
topology_sort()
            