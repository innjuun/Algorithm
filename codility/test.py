# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import random

def solution(A):
    # write your code in Python 3.6
    li = [False for _ in range(100002)]
    li[0] = True
    for i, num in enumerate(A):
        if num >= 1 and num <= 100001:
            li[num] = True
    
    for i, boolean in enumerate(li):
        if not boolean:
            return i

test = [random.randrange(-1000000, 1000000) for _ in range(100000)]
print(solution(test))

asyncio