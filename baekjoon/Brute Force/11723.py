import sys

M = int(sys.stdin.readline())
s = 0
for i in range(M):
    op, *num = sys.stdin.readline().split()
    if len(num) > 0:
        num = int(num[0]) - 1

    if op == "add":
        s = s | (1 << num)
    if op == "remove":
        s = s & ~(1 << num)
    if op == "check":
        if s & (1 << num):
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    if op == "toggle":
        s = s ^ (1 << num)
    if op == "all":
        s = (1 << 20) - 1
    if op == "empty":
        s = 0
