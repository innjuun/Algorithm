class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 999999
        max = 0
        for i in range(len(prices)):
            if prices[i] <= min:
                min = prices[i]
            if prices[i] - min > max:
                max = prices[i] - min
        return max