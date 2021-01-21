N = int(input())

li = list(map(int, input().split()))

count_li = [li.count(i) for i in li]


stack = []
ans = [-1 for i in range(len(li))]
stack.append(0)
for i in range(1, len(li)):
    while stack and count_li[stack[-1]] < count_li[i]:
        ans[stack[-1]] = li[i]
        stack.pop()
    stack.append(i)


for a in ans:
    print(a, end=" ")
