def solution(board):
    ROW = len(board)
    COL = len(board[0])
    max_n = 0

    if ROW == 1:
        return 1 if 1 in board[0] else 0
    if COL == 1:
        return 1 if [1] in board else 0

    for x in range(1, ROW):
        for y in range(1, COL):
            if board[x][y] == 1:
                board[x][y] = n = dp(x, y, board)
                max_n = max(max_n, n)
    return max_n * max_n

def dp(x, y, board):
    return min(board[x - 1][y], board[x][y - 1], board[x - 1][y - 1]) + 1
