def solution(board):
    global ROW
    global COL
    COL = len(board)
    ROW = len(board[0])

    max_n = 1
    for x in range(ROW):
        for y in range(COL):
            if board[y][x] == 1:
                n = square(x, y, board)
                max_n = max(n, max_n)

    return max_n * max_n


def square(x, y, board):
    n = 1
    while x + n < ROW and y + n < COL:
        if board[y][x + n] == 0:
            break
        if board[y + n][x] == 0:
            break
        if board[y + n][x + n] == 0:
            break
        n += 1
    return n


print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
