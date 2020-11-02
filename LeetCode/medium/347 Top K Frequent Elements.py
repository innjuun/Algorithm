
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        heap = []
        for key, value in dic.items():
            heapq.heappush(heap, (-value, key))
        value, key = heapq.heappop(heap)
        value = -value
        cnt = 1
        answer.append(key)
        print(heap)
        while heap:
            if k == cnt:
                break
            value, key = heapq.heappop(heap)
            value = -value
            
            answer.append(key)
            
            cnt += 1
        return answer