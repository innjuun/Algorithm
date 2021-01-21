# using sort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


# using heap
from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(len(nums)):
            heappush(heap, nums[i])

            if len(heap) > k:
                heappop(heap)

        return heappop(heap)
