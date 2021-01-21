a = input()

inp = [i for i in a]
stack = []
sum = 0
count = 1
for i in range(len(inp)):
    if inp[i] == "(":
        stack.append(count)

    elif inp[i] == ")":

        if count - stack[-1] == 1:
            stack.pop()
            sum += len(stack)

        else:
            stack.pop()
            sum += 1

    count += 1


print(sum)
