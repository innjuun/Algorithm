n = int(input())
cases = []
for i in range(n):
    cases.append(input())

stack = []
cnt = 0
ans = []
for case in cases:

    while cnt < int(case):
        cnt += 1
        stack.append(cnt)
        ans.append("+")
    if int(case) == stack[-1]:
        stack.pop()
        ans.append("-")
    else:
        ans = "NO"
        break

if ans != "NO":
    for a in ans:
        print(a)
else:
    print(ans)
