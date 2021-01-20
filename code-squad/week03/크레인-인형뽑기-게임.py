from collections import deque
def solution(board, moves):
    answer = 0
    stack = deque([])
    for move in moves:
        get_level_from_board(move - 1, board, stack)
        answer += update_stack(stack)
    return answer

def get_level_from_board(move, board, stack):
    level = 0
    while level < len(board):
        target = board[level][move]
        if target != 0:
            stack.append(target)
            board[level][move] = 0
            break
        level += 1

def update_stack(stack):
    num_of_pop = 0
    while len(stack) > 1:
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            num_of_pop += 2
        else: break
    return num_of_pop

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))