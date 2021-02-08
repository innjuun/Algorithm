N = int(input())

li = list(map(int, input().split()))
sorted_li = sorted(li)
check = [False for _ in range(N)]
answer = [0 for _ in range(N)]
for i in range(N):
    index = sorted_li.index(li[i])
    while True:
        if check[index] == 0:
            check[index] = True
            answer[i] = index + 1
            break
        elif check[index] != 0:
            index += 1

print(' '.join(map(str, answer)))
    