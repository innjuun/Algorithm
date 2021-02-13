n, m = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        count = 1

        for k in range(m):
            if j + k + 1 < n and array[i][j] == array[i][j + k] and array[i][j + k] == array[i][j + k + 1]:
                count += 1
        if count == m:
            answer += 1
            break

for j in range(n):
    for i in range(n):
        count = 1
        for k in range(m):
            if i + k + 1 < n and array[i][j] == array[i + k][j] and array[i + k][j] == array[i + k + 1][j]:
                count += 1
        if count == m:
            answer += 1
            break

print(answer)