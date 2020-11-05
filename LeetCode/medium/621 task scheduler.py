import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for i in tasks:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        heap = []
        for key, value in dic.items():
            heapq.heappush(heap, [-1 * value, key])
        
        answer = 0
        count = 0
#             for i in heap:
#                 if i[0] > 0:
#                     i[0] -= 1
#             if heap[0][0] == 0:
#                 a = heapq.heappop(heap)
#                 a[1] = -1 * a[1]
#                 if a[1] > 1:

#                     heapq.heappush(heap, [n, (a[1]-1) * -1, a[2]])

#             answer += 1
#             print(heap, answer)
            
        return answer