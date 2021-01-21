N = int(input())

for i in range(N):
    for t in range(N, i + 1, -1):
        print(" ", end="")

    for j in range(i + 1):
        print("*", end="")
    print()
