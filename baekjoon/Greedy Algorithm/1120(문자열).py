A, B = input().split()

count_max = 0  # 같은 문자열의 개수가 가장 많은 것
for j in range(len(B) - len(A) + 1):
    count = 0  # 같은 문자열의 개수
    for i in range(len(A)):
        if A[i] == B[i + j]:
            count += 1
    if count >= count_max:
        count_max = count

count_max = count_max + len(B) - len(A)
result = len(B) - count_max
print(result)
