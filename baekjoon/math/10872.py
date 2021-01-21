N = int(input())

"""
def fac(num):
    if num != 1:
        return num * fac(num-1)
    else:
        return 1
"""


def fac(num):
    sum = 1
    for i in range(1, num + 1):
        sum = i * sum

    return sum


print(fac(N))
