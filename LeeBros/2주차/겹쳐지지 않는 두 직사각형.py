from copy import deepcopy
n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
check = [[False for _ in range(m)] for _ in range(n)]
answer = -99999999


def is_check(check, r1, c1, r2, c2):
    return any(
        [any([check[i][j] for j in range(c1, c2 + 1)]) for i in range(r1, r2 + 1)]
    )


def get_total(r1, c1, r2, c2):
    ret = 0
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            ret += grid[i][j]
    return ret


def get_second_rectangle(check):
    maximum = -9999999
    for r1 in range(n):
        for c1 in range(m):
            for r2 in range(r1, n):
                for c2 in range(c1, m):
                    if is_check(check, r1, c1, r2, c2):
                        break

                    maximum = max(
                        maximum,
                        get_total(r1, c1, r2, c2)
                    )
   
    return maximum


for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                rectangle = get_total(r1, c1, r2, c2)

                checked = deepcopy(check)
                for i in range(r1, r2 + 1):
                    for j in range(c1, c2 + 1):
                        checked[i][j] = True

                second_rectangle = get_second_rectangle(checked)
                answer = max(answer, rectangle + second_rectangle)


print(answer)
