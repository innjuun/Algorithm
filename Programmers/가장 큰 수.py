# from itertools import permutations

# def solution(numbers):
#     permuts = list(permutations(numbers, len(numbers)))
#     li = []
#     for p in permuts:
#         li.append(''.join(map(str, p)))

#     return sorted(li)[-1]
def lambda_key(x):
    return x * 10


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda_key, reverse=True)

    return str(int("".join(numbers)))


solution([3, 30, 34, 5, 9])
