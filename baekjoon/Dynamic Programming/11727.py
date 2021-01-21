N = int(input())

d = [0 for i in range(1000)]


def fib(a):
    d[0] = 1
    d[1] = 3
    if a > 2:
        for i in range(2, a):
            d[i] = d[i - 1] + 2 * d[i - 2]

    return d[a - 1]


print(fib(N) % 10007)
