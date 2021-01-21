class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if dic.get(i):
                dic[i] += 1
            else:
                dic[i] = 1

        for i, j in dic.items():
            if j >= len(nums) / 2:
                return i
