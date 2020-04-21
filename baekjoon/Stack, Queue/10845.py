class Queue:
    def __init__(self):
        self.queue = []

    def push(self, num):
        self.queue.append(num)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.queue:
            return 0
        else:
            return 1

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return -1


N = input()
test = Queue()
result = []

for i in range(int(N)):

    cmd = input()
    if " " in cmd:
        cmd, num = cmd.split()

    if cmd == "push":
        test.push(num)
    elif cmd == "size":
        result.append(test.size())
    elif cmd == "empty":
        result.append(test.empty())
    elif cmd == "pop":
        result.append(test.pop())
    elif cmd == "front":
        result.append(test.front())
    elif cmd == "back":
        result.append(test.back())

for i in result:
    print(i)
