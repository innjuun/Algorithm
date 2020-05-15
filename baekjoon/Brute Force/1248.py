n = int(input())

li = list(input())
num_list = [i for i in range(-10, 11)]


def check(stack):
    for i in range(len(stack)):
        summ = 0
        for j in range(i, len(stack)):
            summ += stack[i][j]
            if summ > 0:
                if sign[i][j] != 1:
                    return False
            elif summ == 0 and sign[i][j] != 0:
                return False
            elif summ < 0 and sign[i][j] != -1:
                return False
    return True


def go(index, start, n, m):
    if index == m and check(stack):
        print(stack)
    for i in range(-10, 11):

        stack.append(i)
        go(i + 1, start + 1, n, m)
        stack.pop()


sign = [[0] * n for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(i, n):
        if li[cnt] == "+":
            sign[i][j] = 1
        if li[cnt] == "0":
            sign[i][j] = 0
        if li[cnt] == "-":
            sign[i][j] = -1

        cnt += 1

stack = []
go(0, 0, -10, 10)
