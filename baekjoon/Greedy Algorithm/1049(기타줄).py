N, M = map(int, input().split())

case_list = []
for i in range(M):
    _list = []

    T, K = map(int, input().split())
    _list.append(T)
    _list.append(K)
    case_list.append(_list)

real_min = 100000
if N // 6 > 0:
    minimum = 0
    for i in range(len(case_list)):
        minimum = case_list[i][0] * int(N // 6)

        if minimum < real_min:
            real_min = minimum
    N = N % 6
else:
    real_min = 0

real_min2 = 100000
for i in range(len(case_list)):
    minimum = 0
    if case_list[i][0] < case_list[i][1] * N:
        minimum = case_list[i][0]
    else:
        minimum = case_list[i][1] * N
    if minimum < real_min2:
        real_min2 = minimum

print(real_min + real_min2)
