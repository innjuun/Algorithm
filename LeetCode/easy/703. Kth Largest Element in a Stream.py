import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.heap = nums
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # print(self.heap)
        
        sub = heapq.heappop(self.heap)
        
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, sub)
        return self.heap[0]