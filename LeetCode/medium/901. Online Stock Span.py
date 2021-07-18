class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            _, amount = self.stack.pop()
            res += amount
        self.stack.append((price, res))
        # print(self.stack)
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
spanner = StockSpanner()
for num in [100,80,60,70,60,75,85]:
    print(spanner.next(num))
    