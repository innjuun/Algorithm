def f(a, c=6, *b, **d):
    print(a, b, c, d)


f(1, 2, 3, x=4)
