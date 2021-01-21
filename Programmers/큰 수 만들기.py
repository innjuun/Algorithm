def solution(number, k):
    stack = []
    tmp = k
    for i in range(len(number)):
        stack.append(number[i])
        while tmp > 0 and i < len(number) - 1 and stack and stack[-1] < number[i + 1]:
            stack.pop()
            tmp -= 1
    if tmp == k:
        return number[:-k]
    return "".join(stack)
