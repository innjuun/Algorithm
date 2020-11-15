class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        answer = []
        def dfs(candidates, target, start):
            # print(stack)
            if sum(stack) > target:
                return
            if sum(stack) == target:
                answer.append(stack[:])
            
            for i in range(start, len(candidates)):
                stack.append(candidates[i])
                dfs(candidates, target, i)
                stack.pop()
            
        dfs(candidates, target, 0)
        return answer
            