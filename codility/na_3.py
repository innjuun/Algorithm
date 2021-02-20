# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict
def solution(A):
    # write your code in Python 3.6
    dic = defaultdict(int)
    answer = []
    for num in A:
        if -num in dic:
            answer.append(abs(num))
        dic[num] = 1
    if answer:
        return max(answer)
    return 0
    # return max(key for key, value in dic.items() if value == True)

solution([3, 2, -2, 5, -3])
solution([1, 1, 2, -1, 2, -1])
solution([1, 2, 3, -4])