# def solution(A, X):
#     N = len(A)
#     if N == 0:
#         return -1
#     l = 0
#     r = N - 1
#     while l < r:
#         m = (l + r) // 2
#         if A[m] > X:
#             r = m - 1
#         elif A[m] == X:
#             return m
#         else:
#             l = m + 1
#     if A[l] == X:
#         return l
#     return -1
# def solution(A, X):
#     N = len(A)
#     if N == 0:
#         return -1
#     l = 0
#     r = N - 1
#     while l < r:
#         m = (l + r) // 2
#         if A[m] > X:
#             r = m
#         else:
#             l = m + 1
#     if A[l] == X:
#         return l
#     return -1
def solution(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        m = (l + r) // 2
        if A[m] < X:
            l = m + 1
        else:
            r = m
    if A[l] == X:
        return l
    return -1

print(solution([1, 2, 5, 9, 9], 5))

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 17, 18, 19, 20, 20], 20))