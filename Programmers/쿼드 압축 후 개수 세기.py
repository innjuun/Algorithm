def solution(arr):
    make_quad(arr)
    answer = [0, 0]
    def dfs(arr):
        flag = all_sum(arr)
        if flag:
            answer[0] += flag[0]
            answer[1] += flag[1]
            return

        for quad in make_quad(arr):
            dfs(quad)
    dfs(arr)
    return answer

def make_quad(arr):
    quad1 = [[arr[i][j] for j in range(len(arr[i])//2)] for i in range(len(arr)//2)]
    quad2 = [[arr[i][j] for j in range(len(arr[i])//2)] for i in range(len(arr)//2, len(arr))]
    quad3 = [[arr[i][j] for j in range(len(arr)//2, len(arr))] for i in range(len(arr)//2)]
    quad4 = [[arr[i][j] for j in range(len(arr)//2, len(arr))] for i in range(len(arr)//2, len(arr))]

    return [quad1, quad2, quad3, quad4]


def all_sum(arr):
    a = sum(sum(row) for row in arr)
    if a == len(arr) ** 2:
        return [0, 1]
    elif a == 0:
        return [1, 0]
    return False