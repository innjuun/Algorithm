N = int(input())
li = []
for i in range(N):
    li.append(list(map(int, input().split())))

A = []
B = []

sum_list = []


def go(index, A, B, n):
    if index == n:

        t1 = 0
        t2 = 0
        if len(A) == n // 2 and len(B) == n // 2:
            for i in range(n // 2):
                for j in range(n // 2):
                    if i == j:
                        continue
                    t1 += li[A[i]][A[j]]
                    t2 += li[B[i]][B[j]]
            sum_list.append(abs(t1 - t2))

        return
    if len(A) > n // 2:
        return
    if len(B) > n // 2:
        return
    A.append(index)
    go(index + 1, A, B, n)
    A.pop()
    B.append(index)
    go(index + 1, A, B, n)
    B.pop()


go(0, A, B, N)
print(min(sum_list))
