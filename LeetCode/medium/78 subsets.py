from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(nums) + 1):
            for c in combinations(nums, i):
                answer.append(list(c))
        return answer