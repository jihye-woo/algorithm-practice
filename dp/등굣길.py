def solution(m, n, puddles):
    puddle_set = set()
    global map
    map = [[0] * (m + 1) for _ in range(n + 1)]
    map[1][1] = 0
    for x, y in puddles:
        puddle_set.add((y, x))

    return dp(n, m, puddle_set)

def dp(y, x, puddle_set):

    if (y, x) in puddle_set:
        return 0

    if x == 1 and y == 1:
        return 1

    if x < 1 or y < 1:
        return 0

    return dp(y, x - 1, puddle_set) + dp(y - 1, x, puddle_set)


