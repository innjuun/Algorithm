class Solution:
    def numSquares(self, n: int) -> int:
        memo = [i for i in range(n+1)]
        i = 1
        while i**2 <= n:
            memo[i**2] = 1
            i += 1
        
        for i in range(n + 1):
            j = 1
            while j ** 2 <= (i//2 + 1):
            
                memo[i] = min(memo[i], memo[i-(j**2)] + 1)
                if memo[i] == 1:
                    break
                j += 1
        # print(memo)
        return memo[n]