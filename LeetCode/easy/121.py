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


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = int(1e9)
        for i in range(len(prices)):
            # print(maximum, minimum)
            if prices[i] < minimum:
                minimum = min(minimum, prices[i])
            elif prices[i] - minimum >= profit:
                profit = max(profit, prices[i] - minimum)

        return profit
