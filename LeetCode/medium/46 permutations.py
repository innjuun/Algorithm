class Solution:
    # from itertools import permutations
    def permute(self, nums):
        answer = []
        stack = []
        visited = [False] * len(nums)
        self.dfs(0, nums, answer, stack, visited)
        return answer
    
    def dfs(self, index, nums, answer, stack, visited):
        if index == len(nums):
            answer.append(stack[:])
            return
        
        for i in range(len(nums)):
            if visited[i] is False:
                visited[i] = True
                stack.append(nums[i])
                self.dfs(index + 1, nums, answer, stack, visited)
                stack.pop()
                visited[i] = False
                
solution = Solution()

solution.permute([1, 2, 3])