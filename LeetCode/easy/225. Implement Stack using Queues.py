from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1.append(x)
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1


from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        temp  = deque()
        
        temp = self.queue1
        self.queue1 = self.queue2
        self.queue2 = temp

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1


from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()