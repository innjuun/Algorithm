import itertools

N = input()
case_list = [0] * len(N)
for i in range(len(N)):
    case_list[i] = N[i]


per_list =list(map(''.join, itertools.permutations(case_list)))
result = -1
for i in per_list:
    if (int(i) % 30 == 0) and (result < int(i)):
        result = int(i)
        print(result)
print(result)


