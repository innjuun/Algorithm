E, S, M = map(int, input().split())

e_count = 0
s_count = 0
m_count = 0

for i in range(1, 100000):
    e_count += 1
    s_count += 1
    m_count += 1
    if e_count > 15:
        e_count -= 15
    if s_count > 28:
        s_count -= 28
    if m_count > 19:
        m_count -= 19
    if e_count == E and s_count == S and m_count == M:
        print(i)
        break
