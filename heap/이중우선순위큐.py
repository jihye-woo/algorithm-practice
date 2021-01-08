import heapq
def solution(operations):
    max_heap = []
    min_heap = []

    visited = dict()

    idx = 0
    for op in operations:
        op = op.split()
        if op[0] == "I":
            heapq.heappush(max_heap, (-int(op[1]), idx))
            heapq.heappush(min_heap, (int(op[1]), idx))
            visited[idx] = False
            idx += 1

        else: # if op[0] == "D":
            if op[1] == "1":
                can_pop(max_heap, visited)

            else: # op[1] == "-1"
                can_pop(min_heap, visited)


    return [-heap_peek(max_heap, visited), heap_peek(min_heap, visited)]

def can_pop(heap, visited):
    while heap:
        popped = heapq.heappop(heap)
        idx = popped[1]
        if not visited[idx]:
            visited[idx] = True
            break

def heap_peek(heap, visited):
    while heap:
        popped = heapq.heappop(heap)
        idx = popped[1]
        if not visited[idx]:
            heapq.heappush(heap, popped)
            return popped[0]
    return 0