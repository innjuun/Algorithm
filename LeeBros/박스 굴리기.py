n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        array[i][j], array[j][i] = array[j][i], array[i][j]
        
for i in range(n):
    for j in range(n//2):
        array[i][j], array[i][n-1-j] = array[i][n-1-j], array[i][j]
                                                                 
for i in range(n):
    print(' '.join(map(str, array[i])))