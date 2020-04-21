str1 = input()
left = [i for i in str1]
right = []


M = int(input())
cases = []
for i in range(M):
    cases.append(input())

for case in cases:
    if case[0] == "L":
        if left:
            right.append(left.pop())
    if case[0] == "D":
        if right:
            left.append(right.pop())
    if case[0] == "B":
        if left:
            left.pop()
    if case[0] == "P":
        left.append(case[2])

for i in range(len(right)):
    left.append(right.pop())

print(''.join(left))
