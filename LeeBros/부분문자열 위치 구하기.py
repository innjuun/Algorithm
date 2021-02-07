N = input()
M = input()
answer = -1
for i in range(len(N)):
    if answer != -1:
        break
    for j in range(len(M)):
        if i + j > len(N) - 1:
            break
        if M[j] != N[i + j]:
            break
        if j == len(M) - 1:
            answer = i
            
print(answer)