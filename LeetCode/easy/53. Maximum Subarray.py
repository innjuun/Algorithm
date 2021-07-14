class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        cache = [0 for _ in range(len(nums))]
        cache[0] = nums[0]
        
        for i in range(1, len(nums)):
        
            cache[i] = max(nums[i], (cache[i-1] + nums[i]))
        
        return max(cache)
            
