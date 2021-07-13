class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while len(stack) == 1 and stack[0] == 0:
                stack.pop()
            while k>0 and stack and stack[-1] > int(num[i]):
                stack.pop()
                k -= 1
            stack.append(int(num[i]))
        while stack and k > 0:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        
        return ''.join(str(i) for i in stack)
        
        

print(Solution().removeKdigits('1234567890', 9))