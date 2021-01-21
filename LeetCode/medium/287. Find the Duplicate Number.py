# hash


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return nums[i]
            else:
                dic[nums[i]] = 1


# set


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sett = set()
        for num in nums:
            if num in sett:
                return num
            else:
                sett.add(num)
