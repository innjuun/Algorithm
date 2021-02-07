start, end = input().split()
answer = 0
for i in range(int(start), int(end) + 1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 3:
        answer += 1
    
print(answer)