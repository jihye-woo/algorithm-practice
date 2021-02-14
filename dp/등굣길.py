
from collections import deque
def solution(m, n, puddles):
    puddle_set = set()
    map = [[0] * (m + 1) for _ in range(n + 1)]
    map[1][1] = 1

    for x, y in puddles:
        puddle_set.add((y, x))

    queue = deque([(1, 1)])

    while queue:
        y, x = queue.popleft()

        if (y, x) in puddle_set:
            continue
        else:
            puddle_set.add((y, x))

        if y < n:
            map[y + 1][x] += map[y][x]
            queue.append((y + 1, x))
        if x < m:
            map[y][x + 1] += map[y][x]
            queue.append((y, x + 1))

    return map[n][m] % 1_000_000_007


