from itertools import permutations
from collections import deque
import copy

def solution(expression):
    answer = 0
    main_stack = parsing(expression)
    orders = permutations(["-", "*", "+"])
    for order in orders:
        result = start(main_stack.copy(), order)
        answer = max(abs(result), answer)
    return answer


def start(main_stack, order):
    while len(main_stack) > 1:
        for op in order:
            main_stack = stack_cal(main_stack, op)
    return main_stack[0]


def parsing(exp):
    front = 0
    parsed = []
    for rear in range(len(exp)):
        if exp[rear] in "+-*":
            parsed.append(int(exp[front:rear]))
            parsed.append(exp[rear])
            front = rear + 1
    parsed.append(int(exp[front:]))
    return parsed


def stack_cal(factors, prereq_op):
    queue = deque(factors)
    stack = [queue.popleft()]

    while len(queue) > 1:
        op, num = queue.popleft(), queue.popleft()
        if op == prereq_op:
            top = stack.pop()
            stack.append(cal(top, op, num))
        else:
            stack.extend([op, num])
    stack.extend(queue)
    return stack


def cal(num1, op, num2):
    if op == "*":
        return num1 * num2
    elif op == "-":
        return num1 - num2
    return num1 + num2


print(solution("50*6-3*2"))
