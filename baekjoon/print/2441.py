N = int(input())

for i in range(N, 0, -1):
    for t in range(i, N, 1):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
