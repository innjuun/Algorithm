# def solution(N, number):
#     res_set = [set([N]), set([N*10 + N, N*N, N+N, N-N]), set(), set(), set(), set(),set(), set()]
#     for i in range(1, 8):
#         res_set[i].add(int((i + 1) * str(N)))
#         for j in range(i):
#             for op1 in res_set[j]:
#                 for op2 in res_set[i-j-1]:
#                     res_set[i].add(op1 * op2)
#                     res_set[i].add(op1 + op2)
#                     res_set[i].add(op1 - op2)
#                     if op2 != 0:
#                         res_set[i].add(op1 // op2)

#         if number in res_set[i]:
#             return i
#     return -1

# solution(5, 31168)




def solution(N, number):
    dp = [set() for _ in range(9)]
    
    dp[1].add(N)
    for i in range(2, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                    dp[i].add(num1 * num2)
    for i in range(1, 9):
        if number in dp[i]:
            return i
    return -1

solution(5, 31168)