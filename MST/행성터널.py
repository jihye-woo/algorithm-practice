import heapq
from sys import stdin

def solution_BJ2887():
    n = int(stdin.readline())
    x, y, z = [], [], []
    edge_heap = []
    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]
    total_value = 0
    num_of_edge = 0

    for i in range(n):
        tmp = stdin.readline().split()
        heapq.heappush(x, [int(tmp[0]), i])
        heapq.heappush(y, [int(tmp[1]), i])
        heapq.heappush(z, [int(tmp[2]), i])

    make_edges(edge_heap, x)
    make_edges(edge_heap, y)
    make_edges(edge_heap, z)

    while num_of_edge < n - 1:
        edge = heapq.heappop(edge_heap)
        if get_next_edge(edge, parent, rank):
            num_of_edge += 1
            total_value += edge[0]

    return total_value

def make_edges(edge_heap, group):
    prev = 0
    for next in range(1, len(group)):
        prev_val = group[prev][0]
        next_val = group[next][0]
        prev_idx, next_idx = group[prev][1], group[next][1]
        heapq.heappush(edge_heap, (abs(prev_val - next_val), prev_idx, next_idx))
        prev = next

def get_next_edge(edge, parent, rank):
    weight, node1, node2 = edge

    if find(parent, node1) != find(parent, node2):
        union(rank, parent, node1, node2)
        return True
    return False

def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(rank, parent, node1, node2):
    root1 = node1
    root2 = node2

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

if __name__ == '__main__':
    solution_BJ2887()
