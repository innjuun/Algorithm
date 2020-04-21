N = input()

N = N.split('-')

for i in range(len(N)):
    N[i] = N[i].split('+')

summary = int(N[0][0])
for i in range(1, len(N)):
    sum = 0
    for j in N[i]:
        sum += int(j)
    summary = summary - sum

print(summary)

