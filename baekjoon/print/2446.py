N = int(input())


for i in range(N):
    for j in range(i):
        print(" ", end='')
    for t in range(2*N-1, 2*i, -1):
        print("*", end='')
    print()
for i in range(2, N+1):
    for j in range(0, N-i, 1):
        print(" ", end="")
    for t in range(0, 2*i-1, 1):
        print("*", end='')
    print()
