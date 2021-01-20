def solution(s):
    answer = []
    local_idx = 0
    for c in s:
        if c == ' ':
            local_idx = 0
            answer.append(c)
        else: # c is something
            if local_idx % 2 == 0:
                answer.append(c.upper())
            else: answer.append(c.lower())
            local_idx += 1

    return ''.join(answer)