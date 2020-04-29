d = [0 for i in range(12)]


def sol(a):
    d[0] = 1
    d[1] = 2
    d[2] = 4
    for i in range(3, a):
        d[i] = d[i-1] + d[i-2] + d[i-3]

    return d[i]


sol(11)
T = int(input())
li = []
for i in range(T):
    print(d[int(input())-1])
