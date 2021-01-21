class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def get_parent(node):
            if parent[node] != node:
                parent[node] = get_parent(parent[node])
            return parent[node]

        def union_parent(node1, node2):
            a = get_parent(node1)
            b = get_parent(node2)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        parent = [i for i in range(len(M))]

        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:

                    a = get_parent(i)
                    b = get_parent(j)

                    if a != b:
                        union_parent(a, b)

        return len({get_parent(i) for i in range(len(M))})
