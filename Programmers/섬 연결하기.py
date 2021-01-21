def solution(n, costs):
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    print(costs)
    answer = 0
    for node1, node2, cost in costs:
        if not is_connected(parent, node1, node2):
            union(parent, node1, node2)
            answer += cost
    # print(answer)

    return answer


def find_parent(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find_parent(parent, parent[node])
    return parent[node]


def is_connected(parent, node1, node2):
    return find_parent(parent, node1) == find_parent(parent, node2)


def union(parent, node1, node2):
    node1_parent = find_parent(parent, node1)
    node2_parent = find_parent(parent, node2)
    if node1_parent < node2_parent:
        parent[node2_parent] = node1_parent
    else:
        parent[node1_parent] = node2_parent


solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]])
