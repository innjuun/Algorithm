from itertools import permutations
from collections import deque

def solution(numbers):
    count = 0
    numbers = list(numbers)
    visited = []
    for i in range(1, len(numbers) + 1):
        permut = set(permutations(numbers, i))
        for p in permut:
            p = int(''.join(p))
            if p not in visited:
                visited.append(p)
                if is_prime_number(p):
                    count += 1

    return count

def is_prime_number(number):
    if number == 1 or number == 0:
        return False
    for i in range(2,number // 2 + 1):
        if number % i == 0:
            return False
    return True


solution("011")