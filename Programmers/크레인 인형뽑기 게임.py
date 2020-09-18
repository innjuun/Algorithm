def solution(board, moves):
    answer = 0
    ret = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                ret.append(board[i][move - 1])
                board[i][move - 1] = 0
                if len(ret) > 1 and ret[-1] == ret[-2]:
                    ret.pop()
                    ret.pop()
                    answer += 2
                break
    return answer


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves) == 4)

