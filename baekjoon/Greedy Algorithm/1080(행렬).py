def change(_list, index_y, index_x):
    for i in range(index_y, index_y+3):
        for j in range(index_x, index_x+3):
            if _list[i][j] == 1:
                _list[i][j] = 
            else:
                _list[i][j] = 1




N, M = map(int, input().split())
A = []
B = []
for i in range(N):
    _list = []
    _list2 = []
    for j in range(M):
        _list.append(0)
        _list2.append(0)
    A.append(_list)
    B.append(_list2)

for i in range(N):
    a = input()
    for j in range(len(a)):
        A[i][j] = int(a[j])

for i in range(N):
    b = input()
    for j in range(len(b)):
        B[i][j] = int(b[j])

change(A,0,0)
change(A,0,1)
print(A, B)


# for i in range(M-3+1):
#     for j in range(N-3+1):

