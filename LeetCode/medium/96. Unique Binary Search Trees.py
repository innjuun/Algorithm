class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(23)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, 23):
            for j in range(i):
                dp[i] += dp[i-j -1] * dp[j]
        
        return dp[n]