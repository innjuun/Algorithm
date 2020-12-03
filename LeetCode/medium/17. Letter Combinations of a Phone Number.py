class Solution:
    phone = {
        2: ["a","b","c"],
        3: ['d','e','f'],
        4: ['g','h','i'],
        5: ['j','k','l'],
        6: ['m','n','o'],
        7: ['p','q','r','s'],
        8: ['t','u','v'],
        9: ['w','x','y','z']
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if digits =="":
            return []
        stack = []
        answer = set()
        def dfs(index):
            if index == len(digits):
                answer.add(''.join(stack))
                return

            for i in range(len(self.phone[int(digits[index])])):
                stack.append(self.phone[int(digits[index])][i])
                dfs(index + 1)
                stack.pop()
        
        dfs(0)
        return list(answer)