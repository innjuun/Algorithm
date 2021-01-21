def GCD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


t = int(input())


for i in range(t):
    li = list(map(int, input().split()))
    li.pop(0)
    sum = 0
    for i in range(0, len(li)):
        for j in range(i + 1, len(li)):
            sum += GCD(li[i], li[j])

    print(sum)
