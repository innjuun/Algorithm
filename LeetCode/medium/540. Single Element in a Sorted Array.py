
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        for i in range(0, len(nums), 2):
            try:
                if nums[i+1] != nums[i]:
                    return nums[i]
            except:
                return nums[i]