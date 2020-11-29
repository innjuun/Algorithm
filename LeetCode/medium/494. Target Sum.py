class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        stack = []
        count = 0
        count = []
        def dfs(index):
            if index == len(nums):
                # print(stack)
                if sum(stack) == S:
                    count.append(1)
                return
            
            stack.append(nums[index])
            dfs(index + 1)
            stack.pop()
            stack.append(-nums[index])
            dfs(index + 1)
            stack.pop()
        
        dfs(0)
        return sum(count)