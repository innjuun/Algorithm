N, M = map(int, input().split())

array = reversed([int(input()) for _ in range(N)])


while True:
    stack = []
    temp_array = []
    for i, bomb in enumerate(array):
        if not stack:
            stack.append(bomb)
        elif stack and stack[-1] == bomb:
            stack.append(bomb)
        else:
            if len(stack) >= M:
                pass
            else:
                temp_array += stack
            stack = []
            stack.append(bomb)
    if stack:
        if len(stack) >= M:
            pass
        else:
            temp_array += stack
    if temp_array == array:
        break
    else:
        array = temp_array

print(len(array))
while array:
    print(array.pop())
            