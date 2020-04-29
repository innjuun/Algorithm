def GCD(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a


N, S = map(int, input().split())

li = list(map(int, input().split()))


real_li = []

for l in li:
    if l-S < 0:
        real_li.append(-(l-S))
    else:
        real_li.append(l-S)

max = real_li[0]

if len(real_li) > 1:
    for i in range(len(real_li)-1):

        max = GCD(max, real_li[i+1])

print(max)
