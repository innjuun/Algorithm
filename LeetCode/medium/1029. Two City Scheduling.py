class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = []
        b = []
        for i, cost in enumerate(costs):
            if cost[0] < cost[1]:
                a.append((cost[0], i))
            elif cost[0] >= cost[1]:
                b.append((cost[1], i))
        print(a, b)
        while len(a) > len(b):
            minimum = 9999
            position = 8888
            i_ = 9999
            for i, (num, pos) in enumerate(a):
                candidate = costs[pos][1] - costs[pos][0]
                if candidate <= minimum:
                    minimum = candidate
                    position = pos
                    i_ = i
            a.pop(i_)
            b.append((costs[position][1], position))
        while len(a) < len(b):
            minimum = 9999
            position = 8888
            i_ = 9999
            for i, (num, pos) in enumerate(b):
                candidate = costs[pos][0] - costs[pos][1]
                if candidate <= minimum:
                    minimum = candidate
                    position = pos
                    i_ = i
            b.pop(i_)
            a.append((costs[position][0], position))
        return sum(i[0] for i in a) + sum(i[0] for i in b)