def check(board, N):
    ans = 1

    for i in range(N):
        cnt = 1
        for j in range(1, N):

            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    for j in range(N):
        cnt = 1
        for i in range(1, N):

            if board[i][j] == board[i - 1][j]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans


N = int(input())

board = [list(input()) for i in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        if j < N - 1:
            board[i][j + 1], board[i][j] = board[i][j], board[i][j + 1]
            temp = check(board, N)
            if ans < temp:
                ans = temp
            board[i][j + 1], board[i][j] = board[i][j], board[i][j + 1]
        if i < N - 1:
            board[i + 1][j], board[i][j] = board[i][j], board[i + 1][j]
            temp = check(board, N)
            if ans < temp:
                ans = temp
            board[i + 1][j], board[i][j] = board[i][j], board[i + 1][j]

print(ans)
