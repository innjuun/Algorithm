N = int(input())
li = list(map(int, input().split()))
answer = []
while True:
    if len(li) == 0:

        break
    maximum = max(li)
    for i, elem in enumerate(li):
        if elem == maximum:
            answer.append(i+1)
            li = li[:i]
            break
    
print(' '.join(map(str, answer)))