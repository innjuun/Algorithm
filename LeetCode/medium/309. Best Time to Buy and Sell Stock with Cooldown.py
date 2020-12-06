class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp_sell = [0 for i in range(len(prices))]
        dp_buy = [0 for i in range(len(prices))]
        dp_cooldown = [0 for i in range(len(prices))]
        
        dp_buy[0] = -prices[0]
        
        for i in range(1, len(prices)):
            dp_buy[i] = max(dp_cooldown[i-1] - prices[i], dp_buy[i-1])
            dp_sell[i] = max(dp_buy[i-1] + prices[i], dp_cooldown[i-1]) 
            dp_cooldown[i] = max(dp_cooldown[i-1], dp_sell[i-1], dp_buy[i-1])

        print(dp_buy)
        print(dp_sell)
        print(dp_cooldown)
        return max(dp_sell[-1], dp_cooldown[-1])
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp_sell = [0 for i in range(len(prices))]
        dp_buy = [0 for i in range(len(prices))]
        dp_cooldown = [0 for i in range(len(prices))]
        
        dp_buy[0] = -prices[0]
        
        for i in range(1, len(prices)):
            dp_buy[i] = max(dp_sell[i-2] - prices[i], dp_buy[i-1])
            dp_sell[i] = max(dp_buy[i-1] + prices[i], dp_sell[i-1]) 
            # dp_cooldown[i] = max(dp_cooldown[i-1], dp_sell[i-1], dp_buy[i-1])

        # print(dp_buy)
        print(dp_sell)
        # print(dp_cooldown)
        return dp_sell[-1]