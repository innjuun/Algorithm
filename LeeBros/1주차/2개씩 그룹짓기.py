N = input()
li = list(map(int, input().split()))

li.sort()
answer = 0
for i in range(len(li)//2):
    answer = max(answer, li[i] + li[len(li)-1-i])

print(answer)