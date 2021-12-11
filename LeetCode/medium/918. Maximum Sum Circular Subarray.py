class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if all(n < 0 for n in nums):
            return max(nums)
        
        return max(self.get_maximum(nums), (sum(nums) - self.get_minimum(nums)))
        
    def get_minimum(self, nums):
        if len(nums) == 1:
            return nums[0]
        cache = [2e9 for _ in range(len(nums))]
        cache[0] = nums[0]
        for i in range(1, len(nums)):
            cache[i] = min(nums[i], cache[i-1] + nums[i])
        # print(cache)
        return min(cache)

    def get_maximum(self, nums):
        if len(nums) == 1:
            return nums[0]
        cache = [0 for _ in range(len(nums))]
        cache[0] = nums[0]
        
        for i in range(1, len(nums)):
            cache[i] = max(nums[i], cache[i-1] + nums[i])
        return max(cache)
        
