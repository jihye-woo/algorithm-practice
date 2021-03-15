from collections import deque

def solution(p):
    answer = ''

    # [1] is empty?
    if not p:
        return answer

    # [2] w = u + v
    u, v = param_pairs(p)

    # [3] check u
    if is_right_string(u):
        return u + solution(v)

    # [4] edit u string
    else:
        return '(' + solution(v) + ')' + reform(u)


def reform(u):
    if len(u) < 2: return []

    reformed = ''
    for param in u[1:-1]:
        reformed += '(' if param == ')' else ')'

    return reformed

def param_pairs(p):
    param_counter = 0
    v = p
    u = ''

    while True:
        param = v[0]
        param_counter += 1 if param == '(' else -1

        # update u and v
        v = v[1:]
        u += param

        if param_counter == 0 or len(v) == 0:
            break
    return u, v

def is_right_string(w):
    stack = []
    w = deque(w)

    while len(w) > 0:
        stack.append(w.popleft())
        if len(stack) >= 2:
            if stack[-2] + stack[-1] == '()':
                stack.pop()
                stack.pop()

    return stack == []

print(solution("(()())()"))

