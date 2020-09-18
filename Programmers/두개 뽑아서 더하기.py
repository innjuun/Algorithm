from itertools import combinations


def solution(numbers):
    answer = set()
    comb = combinations(numbers, 2)
    for a, b in comb:
        answer.add(a + b)
    return sorted(list(answer))
