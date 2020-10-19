a = int(input())
checked = [0] * (a+1)
checked[1] = 1
checked[2] = 1
checked[3] = 1
checked[4] = 2
checked[5] = 1
checked[6] = 2
i = 1

for i in range(7, a):
    li = []
    if i % 5 == 0:
        li.append(checked[i//5])
    if i % 3 == 0:
        li.append(checked[i//3])
    if i % 2 == 0:
        li.append(checked[i//2])
    li.append(checked[i-1])
    checked[i] = min(li) + 1

print(checked)