class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        self.cache = {}
        self.nums1 = nums1
        self.nums2 = nums2

        return self.helper(len(nums1) - 1, len(nums2) - 1)
    def helper(self, i, j):
        if i == -1 or j == -1:
            return 0
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        
        if self.nums1[i] == self.nums2[j]:
            self.cache[(i, j)] = self.helper(i-1, j-1) + 1
        else:
            self.cache[(i, j)] = max(self.helper(i-1, j), self.helper(i, j-1))
            
        return self.cache[(i, j)]
