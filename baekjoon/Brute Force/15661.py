N = int(input())
li = []

for i in range(N):
    li.append(list(map(int, input().split())))

sum_list = []


def go(index, A, B, N):

    if index == N:
        if len(A) > 0 and len(B) > 0:
            t1 = 0
            t2 = 0

            for i in range(len(A)):
                for j in range(len(A)):
                    if i == j:
                        continue
                    t1 += li[A[i]][A[j]]
            for i in range(len(B)):
                for j in range(len(B)):
                    if i == j:
                        continue
                    t2 += li[B[i]][B[j]]

            sum_list.append(abs(t1 - t2))

        return

    A.append(index)
    go(index + 1, A, B, N)
    A.pop()

    B.append(index)
    go(index + 1, A, B, N)
    B.pop()


go(0, [], [], N)

print(min(sum_list))
