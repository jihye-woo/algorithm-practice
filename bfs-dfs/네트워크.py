from collections import deque
def solution(n, computers):
    global visited
    visited = set()
    bfs(n, computers)
    return n - len(visited) + 1

def bfs(n, computers):
    queue = deque([0])
    total = {i for i in range(1, n)}
    rest = total - set()
    while rest:
        while queue:
            target = queue.popleft()
            visited.add(target)
            for i in range(n):
                if computers[target][i] and i not in visited:
                    queue.append(i)

        rest = total - visited
        if rest:
            queue.append(rest.pop())
        else: break

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
