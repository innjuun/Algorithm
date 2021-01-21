def next_permutation(li):
    n = len(li)
    i = n - 1
    j = n - 1
    while i > 0:
        if li[i] > li[i - 1]:
            break
        i -= 1
    if i <= 0:
        return False
    while i <= j:
        if li[j] > li[i - 1]:
            break
        j -= 1

    li[i - 1], li[j] = li[j], li[i - 1]
    j = n - 1
    while i < j:
        li[i], li[j] = li[j], li[i]
        i += 1
        j -= 1

    return True


n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

a = [i for i in range(n)]


minimum = 1000000000

while True:
    if a[0] != 0:
        break
    ok = True
    sum = 0
    for i in range(n - 1):
        if li[a[i]][a[i + 1]] == 0:
            ok = False
            break
        else:
            sum += li[a[i]][a[i + 1]]

    if li[a[-1]][a[0]] != 0 and ok:

        sum += li[a[-1]][a[0]]

        minimum = min(sum, minimum)

    if not next_permutation(a):
        break

print(minimum)
