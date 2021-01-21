N = int(input())

for i in range(N):
    for t in range(i, N - 1, 1):
        print(" ", end="")
    for j in range(i):
        print("**", end="")
    print("*", end="")
    print()
