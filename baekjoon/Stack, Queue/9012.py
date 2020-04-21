T = int(input())
cases = []
for i in range(T):
    cases.append(input())
for case in cases:
    stack = 0
    for char in case:

        if char == "(":
            stack += 1
        elif char == ")":
            stack -= 1
        if stack < 0:
            break
    if stack == 0:
        print("YES")
    else:
        print("NO")
