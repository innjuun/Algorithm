L, C = map(int, input().split())
li = list(input().split())

li.sort()


a = []
vowel = ["a", "e", "i", "o", "u"]


def check(li):
    mo = 0
    ja = 0
    for t in li:
        if t in vowel:
            mo += 1
        else:
            ja += 1

    if mo >= 1 and ja >= 2:
        return True


def go(index, start, n, m):
    if index == m:
        if check(a):
            print("".join(a))

        return
    for i in range(start, n):
        a.append(li[i])
        go(index + 1, i + 1, n, m)
        a.pop()


go(0, 0, C, L)
