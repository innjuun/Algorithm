n = int(input())

li = list(map(int, input().split()))


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


if next_permutation(li):
    print(" ".join(map(str, li)))
else:
    print("-1")
