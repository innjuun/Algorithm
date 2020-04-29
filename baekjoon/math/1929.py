"""
M, N = map(int, input().split())

prime = []
pn = 0
check = [i for i in range(N)]

for i in range(M, N):
    for j in range(2, i):
        if i % j == 0:
            check[i] = False
            break


for i in check:
    if i and i >= M:
        print(i)
"""
import math
flag = True
li = []
while flag:
    a = int(input())

    if a == 0:
        flag = False
    else:
        li.append(a)


def isPrime(num):
    if num == 1:
        return False

    n = int(math.sqrt(num))
    for i in range(2, n+1):
        if num % i == 0:
            return False
    return True


max = 0
i1 = 0
i2 = 0
for num in li:
    for i in range(2, num):
        if isPrime(i):
            if isPrime(num-i):

                print(f"{num} = {i} + {num - i}")
                break
