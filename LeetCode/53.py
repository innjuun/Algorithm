from typing import List


def maxSubArray(nums: List[int]) -> int:
    memoi_list = [-9999999 for i in range(len(nums))]
    memoi_list[0] = nums[0]
    
    for i in range(1, len(nums)):
        if memoi_list[i-1] + nums[i] > nums[i]:
            memoi_list[i] = memoi_list[i-1] + nums[i]
        else:
            memoi_list[i] = nums[i]
    return max(memoi_list)

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
