N = input()
elements  = [str(0) for _ in range(21)]
elements[1] = str(1)
for i in range(2, 21):
    item = ""
    stack = []
    for j in range(len(elements[i-1])):
        if stack and elements[i-1][j] != stack[-1]:
            item += stack[-1]
            item += str((len(stack)))
            stack = [elements[i-1][j]]
        else:
            stack.append(elements[i-1][j])

    item += stack[-1]
    item += str((len(stack)))
    elements[i] = item

print(elements[N]) 