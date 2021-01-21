"""
N = input()
nge = input().split()


left = []
right = [i for i in nge]
left.append(right.pop(0))
maximum = []
for i in range(int(N)-1):

    for j in range(len(right)):
        if right[j] > left[-1]:
            maximum.append(right[j])
            break
    if left[-1] > max(right):
        maximum.append(-1)
    if i != N:
        left.append(right.pop(0))

maximum.append(-1)
print(maximum)
"""

N = input()
nge = input().split()

li = [int(i) for i in nge]
stack = []
ans = [0 for i in range(len(li))]
stack.append(0)

for i in range(1, len(li)):
    if not stack:
        stack.append(i)

    while stack and (li[stack[-1]] < li[i]):
        ans[stack[-1]] = li[i]
        stack.pop()

    stack.append(i)


while stack:
    ans[stack[-1]] = -1

    stack.pop()

for a in ans:
    print(a, end=" ")
