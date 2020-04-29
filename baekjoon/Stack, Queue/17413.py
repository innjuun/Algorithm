S = input()
whole = []
for i in S:
    whole.append(i)
tags = False
stack = []
for char in whole:
    if char == "<" and stack:
        while stack:
            print(stack.pop(), end="")
    if char == "<":
        print(char, end='')
        tags = True
    elif char == ">":
        print(char, end='')
        tags = False
    elif tags:
        print(char, end='')
    elif char == " ":
        while stack:
            print(stack.pop(), end="")
        print(char, end="")
    else:
        stack.append(char)
while stack:
    print(stack.pop(), end="")
