n = int(input())

li = list(map(int, input().split()))


def prev_permutation(li):
    n = len(li)
    i = n - 1
    j = n - 1
    while i > 0:
        if li[i - 1] > li[i]:
            break
        i -= 1
    if i <= 0:
        return False
    while j >= i:
        if li[i - 1] > li[j]:
            break
        j -= 1
    li[i - 1], li[j] = li[j], li[i - 1]

    t = n - 1
    while i < t:
        li[i], li[t] = li[t], li[i]
        i += 1
        t -= 1
    return True


if prev_permutation(li):
    print(" ".join(map(str, li)))
else:
    print("-1")
