import heapq
def solution(n, costs):
    answer = 0
    visited = set()
    ranks = [0 for i in range(n)]
    roots = [i for i in range(n)]
    edges = []
    for n1, n2, cost in costs:
        heapq.heappush(edges, (cost, n1, n2))

    while edges:
        cost, n1, n2 = heapq.heappop(edges)
        # if n1 and n2 are already visited
        if n1 in visited and n2 in visited:
            # check the root of the n1 and n2
            # [if same root] n1 and n2 are already in the same group
            # so, this edge make a cycle => pass
            # [else] n1 and n2 have diff root
            if roots[n1] != roots[n2]:
                add_edge(roots, n1, n2, visited)
                answer += cost

        else:
            add_edge(roots, n1, n2, visited)
            answer += cost
    return answer

def add_edge(roots, n1, n2, visited):
    root1, root2 = roots[n1], roots[n2]
    # root1보다 root2가 더 작다면
    # root1이 우선순위가 더 높기 때문에 root2가 root였던 노드들의 root를 root1으로 바꿔준다.
    if root1 < root2:
        change_root(roots, root2, root1)
    else:
        change_root(roots, root1, root2)
    visited.add(n1)
    visited.add(n2)

# change root2를 root로 가진 노드들의 root = root1
def change_root(roots, from_root, to_root):
    for i in range(len(roots)):
        if roots[i] == from_root:
            roots[i] = to_root




print(solution(		5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))