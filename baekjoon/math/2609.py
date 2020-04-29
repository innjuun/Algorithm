def GCD(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r

    return a


def LCM(a, b):
    return int(a * b / GCD(a, b))


a, b = map(int, input().split())
print(GCD(a, b))
print(LCM(a, b))
