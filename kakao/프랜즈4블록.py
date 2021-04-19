from collections import defaultdict

block = [(0, 1), (1, 0), (1, 1)]


def solution(m, n, board):
    global M, N, answer
    tmp_board = [list(row) for row in board]
    answer = 0
    M, N = m, n

    candidates = defaultdict(set)  # { column1 : [row1, row2, ...], column2 : [row1, row2, ... ],  } # pop을 할 대상

    while True:

        marked = [ [True for i in range(N)] for i in range(M) ]
        for r in range(m - 1):
            for c in range(n - 1):
                if find_four_blocks(r, c, tmp_board):
                    marked[r][c] = False
                    marked[r][c + 1] = False
                    marked[r + 1][c] = False
                    marked[r + 1][c + 1] = False

    # pop if False in marked array
        pop_num = pop_board(tmp_board, marked)
        if pop_num == 0:
            break

        answer += pop_num

        for col in range(N):
            move_board(col, tmp_board)

    return answer


def find_four_blocks(row, col, board):
    target = board[row][col]

    if row >= M - 1 or col >= N - 1 or not target:  # cannot check 2 * 2 blocks
        return False

    for dx, dy in block:
        if board[row + dx][col + dy] != target:
            return False
    return True

def pop_board(tmp_board, marked):
    counter = 0
    for i in range(M):
        for j in range(N):
            if not marked[i][j]:
                tmp_board[i][j] = None
                counter += 1
    return counter

def move_board(col, board):
    for idx in range(M - 1, 1, -1):
        if not board[idx][col]:
            for target in range(idx - 1, -1, -1):
                if board[target][col]:
                    board[idx][col], board[target][col] = board[target][col], board[idx][col]
                    break

def print_board(board):
    for row in board:
        print(row)
    print()


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
