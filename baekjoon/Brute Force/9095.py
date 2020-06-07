T = int(input())


def go(s, goal):
    if s > goal:
        return 0
    if s == goal:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(s + i, goal)
    return now


for i in range(T):
    n = int(input())
    a = []
    print(go(0, n))
