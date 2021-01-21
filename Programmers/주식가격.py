# brute force
# def solution(prices):
#     answer = [0 for _ in range(len(prices))]

#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[j] >= prices[i]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break


#     return answer

# stack


def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top

    return answer


solution([1, 2, 3, 2, 3])
