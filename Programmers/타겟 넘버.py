# cnt = 0


# def solution(numbers, target):
#     dfs(0, numbers, target, 0)
#     return cnt

# def dfs(index, numbers, target, sum):
#     global cnt
#     if index == len(numbers):
#         if sum == target:
#             cnt += 1
#         return

#     dfs(index+1, numbers, target, sum + numbers[index])
#     dfs(index+1, numbers, target, sum - numbers[index])

# solution([1, 1, 1, 1, 1], 3)


# better solution, not using f
def solution(numbers, target):
    answer = dfs(0, numbers, target, 0)
    return answer

def dfs(index, numbers, target, sum):
    if index == len(numbers):
        if sum == target:
            return 1
        else:
            return 0

    return dfs(index+1, numbers, target, sum + numbers[index]) + dfs(index+1, numbers, target, sum - numbers[index])

solution([1, 1, 1, 1, 1], 3)
