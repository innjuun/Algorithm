
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
        

# log(n) solution

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        self.nums = nums
        self.binary_search(0, len(nums)-1)
        
        return nums[self.answer]

    def binary_search(self, start, end):
        mid = (start + end) // 2
        # print(start, end, mid)
        if start == end:
            self.answer = mid
            return
        # print(mid % 2 == 1 and self.nums[mid] == self.nums[mid-1])
        if (mid % 2 == 1 and self.nums[mid] == self.nums[mid-1]) or (mid % 2 == 0 and self.nums[mid] == self.nums[mid+1]):
            self.binary_search(mid + 1, end)
        else:
            self.binary_search(start, mid)
        