n, s = map(int, input().split())

li = list(map(int, input().split()))
count = 0
stack = []


def go(index, selected, n):
    global count
    if index == n:
        if stack and sum(stack) == s:
            count += 1

        return

    stack.append(li[index])
    go(index + 1, selected + 1, n)
    stack.pop()
    go(index + 1, selected, n)


go(0, 0, n)
print(count)
