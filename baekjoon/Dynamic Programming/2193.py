N = int(input())

pn = [[0, 0] for i in range(92)]

pn[1][0] = 0
pn[1][1] = 1
pn[2][0] = 1
pn[2][1] = 0
pn[3][0] = 1
pn[3][1] = 1

for i in range(4, 91):
    for j in range(2):
        if j == 0:
            pn[i][1] += pn[i - 1][0]
            pn[i][0] += pn[i - 1][0]
        else:
            pn[i][0] += pn[i - 1][1]

result = pn[N][0] + pn[N][1]
print(result)
