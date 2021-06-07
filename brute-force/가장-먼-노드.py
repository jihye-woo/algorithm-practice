from collections import defaultdict, deque
def solution(n, edge):
    START_NODE = 1

    graph = defaultdict(list)
    answer = defaultdict(int)

    # adjacency list
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    farthest = 1

    queue = deque([(START_NODE, 0)])
    answer[0] = 1
    visited = {1}

    while queue:
        node, level = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, level + 1))
                visited.add(neighbor)
                answer[level + 1] += 1
                farthest = level + 1

    return answer[farthest]