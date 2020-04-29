N = int(input())


num = 5
sum = 0
while (num <= N):
    sum += int(N/num)
    num = num*5

print(int(sum))
