INF = int(1e10)
class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        minimum = self.getMin()
        if minimum is None or x < minimum:
            minimum = x
        self.stack.append((x, minimum))


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()