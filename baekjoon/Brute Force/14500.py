N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        count = 1
        board_sum = board[i][j]
