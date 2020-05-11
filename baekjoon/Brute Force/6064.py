"""
T = int(input())
li = []
for i in range(T):
    li.append(list(map(int, input().split())))

for l in li:
    m_count = 1
    n_count = 1
    count = 0
    for i in range(1, l[0] * l[1] + 1):
        if m_count > l[0]:
            m_count -= l[0]
        if n_count > l[1]:
            n_count -= l[1]
        count += 1
        if l[2] == m_count and l[3] == n_count:
            print(count)
            break
        m_count += 1
        n_count += 1
        if i == l[0] * l[1]:
            print(-1)
"""


T = int(input())
li = []
for i in range(T):

    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    year = x

    while year < n * m:
        if year % n == y:
            print(year + 1)
            break
        year += m
    else:
        print(-1)
