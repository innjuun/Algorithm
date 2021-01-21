N = int(input())

for i in range(1, N + 1):
    for j in range(i):
        print("*", end="")
    for t in range(2 * N, 2 * i, -1):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
for i in range(1, N + 1):
    for j in range(N - i):
        print("*", end="")
    for t in range(2 * i):
        print(" ", end="")
    for k in range(N - i):
        print("*", end="")
    print()
