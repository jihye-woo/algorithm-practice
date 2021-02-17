def solution(n, computers):
    global visited
    visited = set()
    return dfs(n, computers)

def dfs(n, computers):
    counter = 1
    stack = [0]
    total = {i for i in range(1, n)}
    rest = total - set()
    while rest:
        while stack:
            target = stack.pop()
            visited.add(target)
            for i in range(n):
                if computers[target][i] and i not in visited:
                    stack.append(i)

        rest = total - visited
        if rest:
            stack.append(rest.pop())
            counter += 1
        else: break
    return counter

