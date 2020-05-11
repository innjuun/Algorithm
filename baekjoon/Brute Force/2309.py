import sys
n = 9
li = []
for i in range(n):
    li.append(int(input()))


li_sum = sum(li)

li.sort()
for i in range(n):
    for j in range(i + 1, n):
        if (li_sum - li[i] - li[j]) == 100:
            for t in range(n):
                if li[t] == li[i] or li[t] == li[j]:
                    continue
                print(li[t])
            sys.exit(0)