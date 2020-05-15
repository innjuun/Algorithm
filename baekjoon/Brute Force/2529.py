def go(index, n):

    if index == n + 1:

        sum_list.append("".join(map(str, st)))

        return
    for i in range(10):
        if check[i] is True:
            continue
        if (
            index == 0
            or (st[index - 1] < i and li[index - 1] == "<")
            or (st[index - 1] > i and li[index - 1] == ">")
        ):
            check[i] = True
            st.append(i)

            go(index + 1, n)
            check[i] = False
            st.pop()


N = int(input())

li = list(input().split())
check = [False] * 10
st = []
sum_list = []

go(0, N)

sum_list.sort()
print(sum_list[-1])
print(sum_list[0])

"""
    for i in range(n):

        for j in range(10):
            if li[i] == "<" or index == 0:
                if j > st[i] and a[j] is False:
                    a[j] = True
                    st[i] = j
                    go(i + 1, n)
                    a[j] = False
                    st[i] = 0
            if li[i] == ">" or index == 0:
                if j < st[i] and a[j] is False:
                    a[j] = True
                    st[i] = j
                    go(i + 1, n)
                    a[j] = False
                    st[i] = 0
"""
