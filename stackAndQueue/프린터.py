import heapq
from collections import deque
def solution(priorities, location):
    answer = 0

    # queue for the priorities
    priorities = deque(priorities)

    # max heap
    max_heap = [-p for p in priorities]
    heapq.heapify(max_heap)
    highest = heapq.heappop(max_heap)

    while priorities:
        target = priorities.popleft()

        # print
        if -highest == target:
            answer += 1
            # print that I want
            if location == 0: return answer
            # check max_heap is None or not
            if max_heap: highest = heapq.heappop(max_heap)
            else: return answer

        # don't print, go back to the queue
        else:
            priorities.append(target)

        # update location value
        location = len(priorities) -1 if location == 0 else (location - 1)

    return answer

