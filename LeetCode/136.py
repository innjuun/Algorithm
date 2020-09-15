class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if dic.get(i):
                dic[i] +=1
            else:
                dic[i] = 1
        
        while dic:
            a, b = dic.popitem()
            if b==1:
                return a