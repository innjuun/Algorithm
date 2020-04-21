N, M, K = map(int, input().split())
team_count = 0
for i in range(K+1):
    T = N-i
    P = M-(K-i)
    if (T or P) < 0:
        continue
    for j in range(P+1):

        if (2 * j <= T) and (team_count <= j):
            team_count = j
            print(T,P, team_count)


print(team_count)
