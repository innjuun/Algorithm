# class Solution:
#     def change(self, amount: int, coins) -> int:
#         self.answer = 0
#         self.amount = amount
#         self.coins = coins
#         self.dfs(0, 0)
#     def dfs(self, total, index):
#         if total >= self.amount:
#             if total == self.amount:
#                 self.answer += 1
#             return
        
#         for i in range(index, len(self.coins)):
#             self.dfs(total + self.coins[i], i)
            

class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [[0 for j in range(amount + 1)] for i in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):

                try:
                    # print(i, j)
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                except:
                    dp[i][j] = dp[i-1][j]
        
        print(dp[-1])
        return dp[-1]
Solution().change(100, [1,101,102,103])