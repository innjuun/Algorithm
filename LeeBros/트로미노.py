n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def is_valid(i, j):
    return i >= 0 and j >= 0 and i < n and j < m

types = [
    [[0, 1], [1, 0], [1, 1]],
    [[0, 0], [0, 1], [1, 0]],
    [[0, 0], [0, 1], [1, 1]],
    [[0, 0], [1, 0], [1, 1]],
    [[0, 0], [0, 1], [0, 2]],
    [[0, 0], [1, 0], [2, 0]],
]

for i in range(n):
    for j in range(m):
        for type in types:
            valid = True
            for nx, ny in type:
                if not is_valid(i + nx, j + ny):
                    valid = False
                    break
            
            if valid:
                total = 0
                for nx, ny in type:
                    total += array[i + nx][j + ny]
                answer = max(total, answer)
                    
print(answer)