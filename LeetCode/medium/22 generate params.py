class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(index, left, right):
            if index == n * 2:
                answer.append(''.join(stack))
                return
            if left < n:
                stack.append('(')
                dfs(index + 1, left + 1, right)
                stack.pop()
            if left > right:
                stack.append(')')
                dfs(index + 1, left, right + 1)
                stack.pop()
        
        stack = []
        answer = []
        dfs(0, 0, 0)
        return answer