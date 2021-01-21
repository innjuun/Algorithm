N = int(input())

for i in range(N):
    if i < N - 1:
        for t in range(1, N - i, 1):
            print(" ", end="")
        if i != 0:
            print("*", end="")
        for k in range(0, 2 * i - 1, 1):
            print(" ", end="")
        print("*")
    else:
        for j in range(0, 2 * N - 1):
            print("*", end="")
