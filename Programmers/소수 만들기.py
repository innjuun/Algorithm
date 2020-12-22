from itertools import combinations

def solution(nums):
    answer = 0
    comb = combinations(nums, 3)
    for c in comb:
        if is_answer(sum(c)):
            answer += 1
    return answer

def is_answer(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True